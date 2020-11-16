
from parametro import Parametro
from catalogoCharla import CatalogoCharla


class ControladorBot:
    def __init__(self):
        self.PARAMETRO = Parametro()
        self.CATALOGO_CHARLA = CatalogoCharla()
        self.charla_actual = None





    def nuevo_mensaje(self, mensaje):
        # "hola quiero un movil"


        # mensaje es una palabra reservada de airtrack
        #       ejecutar accion
        #       salir

        # comentario no es una palabra reservada de airtrack

        # self.charla_actual = self.CATALOGO_CHARLA.buscar(mensaje)
        # no hay charla
            # crearla
            # modo=buscar el modo de parametros
            # segun el modo, llamar a su funcion ver que opciones se guardaran en logs y las acciones
            # guardar en logs que se saludo!
            # armar algo en servicio???
            # enviar mensaje o solo crearlo y que una tarea lo envie, podria setearlo como enviando???
            # salir

        # comentario hay charla
        # self.charla_actual.esta_charla_activa()
        # obtener el modo de la charla
        # verficar si es uan palabra reservada del usuario segun el modo
        #es una palabra del modo
            #realizar accion (o que la realice el modo)
            # segun el modo, llamar a su funcion ver que opciones se guardaran en logs y las acciones
            # guardar en logs que se saludo!
            # armar algo en servicio???
            # enviar mensaje o solo crearlo y que una tarea lo envie, podria setearlo como enviando???
            # salir

        # comentario si no es una palabra del modo
        # si no es una opcion valida
            # self.charla_actual.incrementar_intentos_fallidos()
            # self.charla_actual.validar_intentos_fallidos(self.PARAMETRO.maximo_intentos_fallidos)
        # es una opcion valida
            # setear opcion del log como seleccionada
            # marcar como inactivos las actuales
            # obtener accion a realizar (no buscar en la bd porque si la cambio a la bd en tiempo real se rompera)
            # segun el modo determinar a que funcion llamar









    def finalizar_charla(self,mensaje):
        # ??????????? tendria que obener la charla actual nuevamente???
        self.charla_actual.finalizar_charla(mensaje)
        self.CATALOGO_CHARLA.actualizar(self.charla_actual)
