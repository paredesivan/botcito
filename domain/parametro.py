# from sqlrepositoryparametro import SqlRepositoryParametro
class Parametro:
    def __init__(self, modo, horarios='6,13,20', maximo_intentos_fallidos=3, automatico_encendido=False):
        self.id_empresa = 1
        self.automatico_encendido = automatico_encendido
        self.horarios = horarios
        self.maximo_intentos_fallidos = maximo_intentos_fallidos
        self.id_modo = modo




    def __str__(self):
        return "producto(" \
               "order_id={self.id_empresa}," \
               "id_modo={self.id_modo}" \
               "modo_del_parametro={self.modo_del_parametro})".format(self=self)




    # llamar a sqlalchemy y setear valores
    # try:
    #     parametros=SqlRepositoryParametro.get(self.id_empresa)
    # except:
    #     raise Exception

    def obtener_maximo_intentos_fallidos(self):
        return self.maximo_intentos_fallidos




    def obtener_horarios(self):
        return self.horarios
