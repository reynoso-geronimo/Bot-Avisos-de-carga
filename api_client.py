# api_client.py
import requests

def get_api_data():
    url = 'http://192.168.0.3:3000/api/proximo'
    response = requests.get(url)
    return response

def process_api_data(response):
    if response.status_code == 200:
        data = response.json()
        response_data = data['file']
        return response_data
    else:
        return None

def set_status(id_value, status, notice=None):
    url = 'http://192.168.0.3:3000/api/setstatus/' + str(id_value)
    postBody = {"estado": status}
    
    # Agregar notice al cuerpo de la solicitud si se proporciona
    if notice is not None:
        postBody["notice"] = notice
    
    response = requests.post(url, json=postBody)
    return response