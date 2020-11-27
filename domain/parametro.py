# from sqlrepositoryparametro import SqlRepositoryParametro
class Parametro:
    def __init__(self, horarios='6,13,20',maximo_intentos_fallidos=3,automatico_encendido=False):
        # self.id_empresa=1
        # llamar a sqlalchemy y setear valores
        # try:
        #     parametros=SqlRepositoryParametro.get(self.id_empresa)
        # except:
        #     raise Exception
        self.automatico_encendido = automatico_encendido
        self.horarios = horarios


        self.maximo_intentos_fallidos = maximo_intentos_fallidos



    def obtener_maximo_intentos_fallidos(self):
        return self.maximo_intentos_fallidos

    def obtener_horarios(self):
        return self.horarios
