# from sqlrepositoryparametro import SqlRepositoryParametro
class Parametro:
    def __init__(self, horarios='6,13,20',maximo_intentos_fallidos=3):
        # self.id_empresa=1
        # llamarasqlalchemy y setear valores
        # try:
        #     parametros=SqlRepositoryParametro.get(self.id_empresa)
        # except:
        #     raise Exception

        self.horarios = horarios

        self.maximo_intentos_fallidos = maximo_intentos_fallidos



    def obtener_maximo_intentos_fallidos(self):
        return self.maximo_intentos_fallidos

    def obtener_horarios(self):
        return self.horarios
