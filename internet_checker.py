# internet_checker.py
import requests
import time

def check_internet_connection():
    while True:  # Ejecutar en un bucle infinito hasta que haya conexión a Internet
        try:
            response = requests.get("https://www.google.com", timeout=5)
            if response.status_code == 200:
                return True  # Se ha establecido una conexión a Internet
        except requests.ConnectionError:
            pass  # Continuar verificando en el siguiente intento
        time.sleep(5)  # Esperar 5 segundos antes de realizar la siguiente verificación
