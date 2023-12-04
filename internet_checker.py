# internet_checker.py
import requests
import time

def check_internet_connection(logger):
    while True:
        try:
            response = requests.get("https://www.google.com", timeout=5)
            if response.status_code == 200:
                return True  # Internet connection established
        except requests.ConnectionError as conn_error:
            # Log the specific connection error
            logger.error(f"Connection error: {conn_error}")
            time.sleep(5)  # Wait for 5 seconds before the next attempt
            continue
        except requests.Timeout as timeout_error:
            # Log the specific timeout error
            logger.error(f"Timeout error: {timeout_error}")
            time.sleep(5)  # Wait for 5 seconds before the next attempt
            continue
        except Exception as e:
            # Log other exceptions
            logger.error(f"An error occurred: {str(e)}")
            time.sleep(5)  # Wait for 5 seconds before the next attempt
            continue