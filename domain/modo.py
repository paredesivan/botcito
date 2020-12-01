class Modo():
    def __init__(self, id_modo, nombre, primer_comando):
        self.id_modo = id_modo
        self.nombre = nombre
        self.primer_comando = primer_comando




    def __repr__(self):
        return "modo(" \
               "id_modo={self.id_modo}," \
               "nombre={self.nombre}".format(self=self)




    def saludo(self):
        pass
        # saludo = tag.obtener_saludo()
        # return saludo




    def seleccionar_direccion(self):
        pass
        # direcciones=callprocessor.obtener_direcciones()
        # return direcciones




    def finalizar_servicio(self):
        pass




    def estado_servicio(self):
        pass




    def confirmar_servicio(self):
        pass




    def datos_chofer(self):
        pass




    def cancelar_servicio(self):
        pass
