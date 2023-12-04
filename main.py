import time
from datetime import datetime
import logging
from internet_checker import check_internet_connection
from api_client import get_api_data, process_api_data, set_status
from vpn_checker import check_and_connect_vpn
from connect_sim import connect_sim
from generate_notice import generate_notice
from urllib3.exceptions import ConnectionError, ConnectTimeoutError

# Configure the logging module
logging.basicConfig(level=logging.INFO)

# Create a logger with a specific name
logger = logging.getLogger("Logger")

# Create a formatter to specify the log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a console handler and set the formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Create a file handler and set the formatter
file_handler = logging.FileHandler('log.log')
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

VPN_NAME = 'Conexión Alpha2000'
SLEEP_DURATION = 5

def main():
    try:
        connected_customs = "000"
        start_day = datetime.now().day

        while True:
            try:
                check_internet_connection(logger)

                response = get_api_data()
                api_data = process_api_data(response)

                if api_data:
                    check_and_connect_vpn(VPN_NAME)

                    # Process API data
                    id_value, notice, customs_code, file_name, address, city, notice_date, notice_time = (
                        api_data['id'],
                        api_data['notice'],
                        api_data['customsCode'],
                        api_data['fileName'],
                        api_data['address'],
                        api_data['city'],
                        api_data['noticeDate'],
                        api_data['noticeTime']
                    )

                    # Check if the day has changed
                    if start_day != datetime.now().day:
                        connected_customs = "000"
                        start_day = datetime.now().day

                    if connected_customs != customs_code:
                        success = connect_sim(customs_code)
                        connected_customs = customs_code

                    if success:
                        success_notice = generate_notice(file_name, address, city, notice_date, notice_time)
                        if success_notice:
                            response = set_status(id_value, "ok", notice)
                        else:
                            response = set_status(id_value, "error")

                        if response.status_code == 200:
                            response_data = response.json()
                            logger.info(response_data)
                        else:
                            logger.error(f'Error in the POST request. Response code: {response.status_code}')
                    else:
                        logger.error("Execution of connect_sim was not successful. Stopping...")
                        break
                else:
                    logger.info(f'No notice found to generate. Response code: {response.status_code}')

                time.sleep(SLEEP_DURATION)

            except (ConnectionError, ConnectTimeoutError) as conn_error:
                logger.error(f"Connection error: {conn_error}")
                logger.info("Restarting the loop after a delay.")
                time.sleep(SLEEP_DURATION)
                continue

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
