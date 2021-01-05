from utiles import enviar_por_http


url = "127.0.0.1:60013"


def obtener_direcciones(telefono):
    return enviar_por_http_wrapper("GET", '/cliente_direcciones', telefono)


def agregar_servicio(datos):
    return enviar_por_http_wrapper("POST", '/grabar_servicio', datos)


def cancelar_servicio(id_servicio):
    return enviar_por_http_wrapper("POST", '/anular_o_reactivar_servicio', id_servicio)


def enviar_por_http_wrapper(metodo, route, datos):
    return enviar_por_http(url, metodo, route, datos)
