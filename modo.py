
class Modo(abc.ABC):
    def __init__(self,id,nombre,texto_accion,funcion):
        self.id=id
        self.nombre=nombre
        self.texto_accion=texto_accion
        self.funcion=funcion

    def saludo(self):
        pass
    def seleccionar_direccion(self):
        pass
    def finalizar_servicio(self):
        pass
    def brindar_estado(self):
        pass
    def confirmar(self):
        pass
    def datos_chofer(self):
        pass
    def cancelar_servicio(self):
        pass

