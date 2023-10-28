from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import time

def generate_notice(fileName,address,city,noticeDate,noticeTime):
    try:
        app = Desktop(backend="uia").window(class_name="ThunderRT6FormDC")
        if app.exists():
            # Obtiene el tamaño de la ventana de la aplicación
            window_rect = app.rectangle()
            window_width = window_rect.width()
            window_height = window_rect.height()

            # Calcula las coordenadas del centro de la ventana
            center_x = window_width // 2
            center_y = window_height // 2

            # Envía un clic derecho al centro de la ventana de la aplicación
            app.click_input(coords=(center_x, center_y), button="right")

            # Espera un momento para que puedas ver el resultado
            time.sleep(2)
            app.type_keys("{UP 3}")
            time.sleep(1)
            send_keys(f"~")
            time.sleep(10)
            send_keys("{ESC 3}")
        return True
    except Exception as e:
         # Si hay algún error, imprime el error y devuelve False para indicar que no fue exitoso.
        print(f"Error en generar aviso: {str(e)}")
        send_keys("{ESC 3}")
        return False