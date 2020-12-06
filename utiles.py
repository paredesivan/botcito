import requests


def enviar_por_http(metodo, ruta, datos):
    if metodo == 'POST':
        return requests.post(ruta, data=datos)
    if metodo == 'GET':
        return requests.get(ruta, data=datos)
