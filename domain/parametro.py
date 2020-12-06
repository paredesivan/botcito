class Parametro:

    # le pongo argumentos con valores por defecto porque no voy a crearlo, lo usare para recuperar cosas nomas
    # no necesito crear la clase si me pongo a pensar
    def __init__(self, id_modo=None, id_sucursal=None, maximo_intentos_fallidos=3,
                 automatico_encendido=False, modo=None):
        self.id_sucursal = id_sucursal
        self.automatico_encendido = automatico_encendido
        self.maximo_intentos_fallidos = maximo_intentos_fallidos
        self.id_modo = id_modo
        self.modo = modo




    def __str__(self):
        return str(self.__dict__)
        # return "parametros(" \
        #        "id_sucursal={self.id_sucursal}," \
        #        "id_modo={self.id_modo}" \
        #        "modo_del_parametro={self.modo_del_parametro})".format(self=self)




    # llamar a sqlalchemy y setear valores
    # try:
    #     parametros=SqlRepositoryParametro.get(self.id_empresa)
    # except:
    #     raise Exception

    def obtener_maximo_intentos_fallidos(self):
        return self.maximo_intentos_fallidos
