from modo import Modo
class ModoBasico(Modo):
    def __init__(self,id,nombre,texto_accion,funcion):
        Modo.__init__(self,id,nombre,texto_accion,funcion)

    def saludo(self):
        saludo = tag.obtener_saludo()
        return saludo

    def seleccionar_direccion(self):
        # direcciones=callprocessor.obtener_direcciones()
        # return direcciones
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