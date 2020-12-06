from utiles import enviar_por_http


def obtener_direcciones(telefono):
    return enviar_por_http("GET", '/cliente_direcciones', telefono)


def agregar_servicio(datos):
    return enviar_por_http("POST", '/grabar_servicio', datos)


def cancelar_servicio(id_servicio):
    return enviar_por_http("POST", '/anular_o_reactivar_servicio', id_servicio)


def obtener_estado_servicio(id_servicio):
    return
