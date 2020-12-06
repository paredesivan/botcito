class Log:
    def __init__(self, datos, id_charla, estado, seleccionado, texto_ofrecido, fecha_hora_envio, opcion, estado_envio):
        self.datos = datos
        self.id_charla = id_charla
        self.estado = estado
        self.seleccionado = seleccionado
        self.texto_ofrecido = texto_ofrecido
        self.fecha_hora_envio = fecha_hora_envio
        self.opcion = opcion
        self.estado_envio = estado_envio




    def __repr__(self):
        return "log(" \
               "id_charlaMadre={self.id_charla}," \
               "opcion={self.opcion}".format(self=self)




    def actualizar_estado(self):
        pass
        # deberia actualizar los datos del objeto o de la bd?




    def seleccionado(self):
        # deberia buscar la opcion disponible y ponerla como seleccionada
        pass
