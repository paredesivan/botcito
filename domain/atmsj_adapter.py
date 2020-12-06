from utiles import enviar_por_http


def enviar_mensaje(mensaje):
    return enviar_por_http("POST", '/enviar_mensaje', mensaje)
