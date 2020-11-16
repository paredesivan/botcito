class Log:
    def __init__(self, datos):
        self.id = datos['id']
        self.estado = datos['estado']
        self.seleccionado = datos['seleccionado']
        self.texto_ofrecido = datos['texto_ofrecido']
        self.fecha_hora_envio = datos['fecha_hora_envio']
        self.opcion = datos['opcion']
        self.estado_envio = ['estado_envio']

    def actualizar_estado(self):
        pass
        # deberia actualizar los datos del objeto o de la bd?

    def seleccionado(self):
        # deberia buscar la opcion disponible y ponerla como seleccionada
        pass
