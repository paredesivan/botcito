import requests


def enviar_por_http(url, metodo, ruta, datos):
    _ruta = url + ruta
    if metodo == 'POST':
        return requests.post(_ruta, data=datos)
    if metodo == 'GET':
        return requests.get(_ruta, data=datos)
