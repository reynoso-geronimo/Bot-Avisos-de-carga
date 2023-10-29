import subprocess
from pywinauto import Desktop
import pyautogui
import time

def is_vpn_connected(vpnname):
    # Ejecuta el comando de PowerShell para verificar el estado de la conexión VPN
    result = subprocess.run(["powershell", f"$vpn = Get-VpnConnection -AllUserConnection | Where-Object {{ $_.Name -eq '{vpnname}' }}; if ($vpn -and $vpn.ConnectionStatus -eq 'Connected') {{ exit 0 }} else {{ exit 1 }}"], text=True)
    
    # Retorna True si la conexión VPN está activa (código de salida 0), de lo contrario retorna False (código de salida 1)
    return result.returncode == 0

def connect_to_vpn():
    
    # Espera unos segundos para dar tiempo a que la barra de tareas se cargue completamente.
    time.sleep(5)

    # Encuentra las coordenadas del botón de Redes en la barra de tareas.
    button_position = pyautogui.locateOnScreen('uielements/red.png')

    if button_position is not None:
        # Calcula el centro del botón de Redes.
        x, y, width, height = button_position
        center_x = x + width // 2
        center_y = y + height // 2

        # Haz clic en el centro del botón de Redes.
        pyautogui.click(center_x, center_y)
        time.sleep(2)  # Pausa de 2 segundos

    else:
        print("No se encontró el botón de Redes en la barra de tareas.")
    
    # Encuentra las coordenadas del botón de Redes en la barra de tareas.
    button_position = pyautogui.locateOnScreen('uielements/vpn.png')

    if button_position is not None:
        # Calcula el centro del botón de Redes.
        x, y, width, height = button_position
        center_x = x + width // 2
        center_y = y + height // 2

        # Haz clic en el centro del botón de Redes.
        pyautogui.click(center_x, center_y)
        time.sleep(2)  # Pausa de 2 segundos

    else:
        print("No se encontró el botón de Redes en la barra de tareas.")
    
    # Encuentra las coordenadas del botón de Redes en la barra de tareas.
    button_position = pyautogui.locateOnScreen('uielements/conectar.png')

    if button_position is not None:
        # Calcula el centro del botón de Redes.
        x, y, width, height = button_position
        center_x = x + width // 2
        center_y = y + height // 2

        # Haz clic en el centro del botón de Redes.
        pyautogui.click(center_x, center_y)
    else:
        print("No se encontró el botón de Redes en la barra de tareas.")
    button_position = pyautogui.locateOnScreen('uielements/red.png')

    if button_position is not None:
        # Calcula el centro del botón de Redes.
        x, y, width, height = button_position
        center_x = x + width // 2
        center_y = y + height // 2

        # Haz clic en el centro del botón de Redes.
        pyautogui.click(center_x, center_y)
        time.sleep(2)  # Pausa de 2 segundos

    else:
        print("No se encontró el botón de Redes en la barra de tareas.")


def check_and_connect_vpn(vpnname):
    if not is_vpn_connected(vpnname):
        print("La VPN no está conectada. Conectando a la VPN...")
        connect_to_vpn()
    else:
        print("La VPN está conectada.")
