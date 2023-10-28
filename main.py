import time
from internet_checker import check_internet_connection
from api_client import get_api_data, process_api_data, set_status
from vpn_checker import check_and_connect_vpn
from connect_sim import connect_sim
from generate_notice import generate_notice
def main():
    try:
        vpnname = 'Conexión Alpha2000'
        connectedCustoms = "000"
        success = True

        while success:
            if check_internet_connection():
                response = get_api_data()
                api_data = process_api_data(response)
                if api_data:
                    check_and_connect_vpn(vpnname)
                    print(api_data)
                    id_value = api_data['id']
                    notice = api_data['notice']
                    customsCode = api_data['customsCode']
                    fileName= api_data['fileName']
                    address= api_data['address']
                    city= api_data['city']
                    noticeDate= api_data['noticeDate']
                    noticeTime= api_data['noticeTime']
                    if connectedCustoms != customsCode:
                        success = connect_sim(customsCode)
                        connectedCustoms = customsCode

                    if success:
                        succes_notice= generate_notice(fileName,address,city,noticeDate,noticeTime)
                        if succes_notice:
                            response = set_status(id_value,"ok",notice)
                        else:
                            response = set_status(id_value,"error")
                        if response.status_code == 200:
                            response_data = response.json()
                            print(response_data)
                        else:
                            print(f'Error en la solicitud POST. Código de respuesta: {response.status_code}')
                    else:
                        print("La ejecución de connect_sim no fue exitosa. Deteniendo...")
                        break
                else:
                    print(f'No se encontro aviso para generar. Código de respuesta: {response.status_code}')
            else:
                print("No hay conexión a Internet. Esperando para volver a verificar...")

            time.sleep(5)

    except Exception as e:
        # Captura la excepción
        print(f"Se ha producido un error: {str(e)}")
        input("Presiona Enter para salir...")
if __name__ == "__main__":
    main()
main()
