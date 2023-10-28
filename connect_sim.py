from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import time

def connect_sim(customsCode):
    try:
        # Busca la ventana principal por su nombre de clase
        app = Desktop(backend="uia").window(class_name="ThunderRT6FormDC")

        if app.exists():
            
            app.type_keys("+{F2}")
            app.type_keys("^a")  # Envía "Ctrl + A" a la ventana
            print("Nombre de la ventana:", app.window_text())
            # Espera a que aparezca la ventana "Conexión con clave fiscal" dentro de la aplicación
            while True:
                app_conexion = app.window(title="Conexión con clave fiscal")
                if app_conexion.exists():
                    break
                time.sleep(1)

            # Espera a que aparezca el elemento con AutomationId igual a "F1:username" dentro de la ventana "Conexión con clave fiscal"
            while True:
                elemento_username = app_conexion.child_window(auto_id="F1:username", control_type="Edit")
                if elemento_username.exists():
                    break
                time.sleep(1)

            # Envía el valor de customsCode al elemento "F1:username"
            elemento_username.type_keys("20241466559~")

            # Espera a que aparezca el elemento "F1:password" y envía la contraseña
            while True:
                elemento_userpassword = app_conexion.child_window(auto_id="F1:password", control_type="Edit")
                if elemento_userpassword.exists():
                    elemento_userpassword.type_keys("Dimaca091218")  # Envía la contraseña
                    break
                time.sleep(1)

            # Espera a que aparezca el primer botón "Ingresar" dentro de la ventana "Conexión con clave fiscal"
            while True:
                boton_ingresar_1 = app_conexion.child_window(title="Ingresar", control_type="Button")
                if boton_ingresar_1.exists():
                    break
                time.sleep(1)

            # Haz clic en el primer botón "Ingresar"
            boton_ingresar_1.click()

            # Espera a que aparezca el segundo botón "Ingresar" dentro de la ventana "Conexión con clave fiscal"
            while True:
                boton_ingresar_2 = app_conexion.child_window(title="Ingresar", control_type="Button")
                if boton_ingresar_2.exists():
                    break
                time.sleep(1)

            # Haz clic en el segundo botón "Ingresar"
            boton_ingresar_2.click()

            # Espera a que aparezca el elemento con AutomationId igual a "3" y envía el valor de customsCode
            # Agrega un retraso de 5 segundos antes de enviar las pulsaciones
            time.sleep(5)

            # Envía las pulsaciones de teclado al elemento deseado
            send_keys(f"{customsCode}~")  # "~" simula la tecla "Enter"
            # Espera 5 segundos
            time.sleep(5)

            send_keys(f"~")
            time.sleep(5)

            # Espera a que la ventana cambie antes de obtener su nombre
            while app.window_text() == "SIM Versión 6.9.0":
                time.sleep(1)
            print("Nombre de la ventana después de enviar Enter:", app.window_text())
            return True

            # ...
    except Exception as e:
        # Si hay algún error, imprime el error y devuelve False para indicar que no fue exitoso.
        print(f"Error en connect_sim: {str(e)}")
        return False
