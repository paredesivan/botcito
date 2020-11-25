class Modo(abc.ABC):
    def __init__(self, id, nombre, texto_accion, funcion):
        self.id = id
        self.funcion = funcion
        self.nombre = nombre
        self.texto_accion = texto_accion





    def saludo(self):
        pass




    def seleccionar_direccion(self):
        pass




    def finalizar_servicio(self):
        pass




    def estado_servicio(self):
        pass




    def confirmar(self):
        pass




    def datos_chofer(self):
        pass




    def cancelar_servicio(self):
        pass
