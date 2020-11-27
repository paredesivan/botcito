from domain.modo import Modo
class ModoBasico(Modo):
    def __init__(self,id_modo,nombre,texto_accion,funcion):
        Modo.__init__(self,id_modo,nombre,texto_accion,funcion)

    def saludo(self):
        saludo = tag.obtener_saludo()
        return saludo

    def seleccionar_direccion(self):
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