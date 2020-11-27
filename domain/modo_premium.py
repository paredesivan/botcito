from domain.modo import Modo


class ModoPremium(Modo):
    def __init__(self,id_modo,nombre,texto_accion,funcion):
        Modo.__init__(self,id_modo,nombre,texto_accion,funcion)

    def saludo(self):
        pass

    def seleccionar_direccion(self):
        pass

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