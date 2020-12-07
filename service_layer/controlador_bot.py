from service_layer.catalogo_charla import CatalogoCharlas
from service_layer.catalogo_parametro import CatalogoParametros
from single import singleton
from domain.charla import Charla
from domain.excepciones import ElementoVacio
from adapters.sql_repository_nodo import SqlRepositoryNodo


def es_mensaje_invalido(mensaje):
    return mensaje is None


@singleton
class ControladorBot:
    def __init__(self, sesion):

        self.CATALOGO_CHARLA = CatalogoCharlas(sesion)
        self.CATALOGO_PARAMETROS = CatalogoParametros(sesion)
        self.SQL_REPOSITORY_NODO = SqlRepositoryNodo(sesion)
        self.parametro_actual = None
        self.charla_actual = None
        self.sesion = sesion




    def existe_charla(self):
        return self.charla_actual is not None and self.charla_actual != 0




    def nuevo_mensaje(self, mensaje):

        if es_mensaje_invalido(mensaje):
            raise ElementoVacio("no hay mensaje")

        # mensaje es una palabra reservada de airtrack
        #       ejecutar accion
        #       salir

        self.charla_actual = self.CATALOGO_CHARLA.buscar_charla_existente(mensaje.get('telefono_origen'))

        if not self.existe_charla():
            self.crear_charla(mensaje)

        ultimo_nodo = self.charla_actual.ultimo_nodo
        menu = ultimo_nodo.armar_menu(self.charla_actual)

        # self.charla_actual.guardar_logs(menu)

        print(self.charla_actual)
        return {'Dato': str(self.charla_actual)}

        # segun el modo, llamar a su funcion ver que opciones se guardaran en logs y las acciones
        # guardar en logs que se saludo!
        # armar algo en servicio???
        # enviar mensaje o solo crearlo y que una tarea lo envie, podria setearlo como enviando???
        # salir

        # comentario: hay charla
        # self.charla_actual.esta_charla_activa()
        # obtener el modo de la charla
        # verficar si es uan palabra reservada del usuario segun el modo
        # es una palabra del modo
        # realizar accion (o que la realice el modo)
        # segun el modo, llamar a su funcion ver que opciones se guardaran en logs y las acciones
        # guardar en logs que se saludo!
        # armar algo en servicio???
        # enviar mensaje o solo crearlo y que una tarea lo envie, podria setearlo como enviando???
        # salir

        # comentario: si no es una palabra del modo
        # si no es una opcion valida
        # self.charla_actual.incrementar_intentos_fallidos()
        # self.charla_actual.validar_intentos_fallidos(self.PARAMETRO.maximo_intentos_fallidos)
        # si es una opcion valida
        # setear opcion del log como seleccionada
        # marcar como inactivos las actuales
        # obtener accion a realizar (no buscar en la bd porque si la cambio a la bd en tiempo real se rompera)
        # segun el modo determinar a que funcion llamar




    def crear_charla(self, mensaje):
        self.parametro_actual = self.CATALOGO_PARAMETROS.buscar()
        if self.parametro_actual == 0:
            raise ElementoVacio("no existe el parametro")

        id_modo_actual = self.parametro_actual.id_modo

        nodo_inicial = self.SQL_REPOSITORY_NODO.obtener_nodo_inicial(id_modo_actual)

        # crea una charla
        try:
            self.charla_actual = Charla(telefono_destino=mensaje.get('telefono_destino'),
                                        telefono_origen=mensaje.get('telefono_origen'),
                                        id_modo=self.parametro_actual.id_modo,
                                        ultimo_nodo=nodo_inicial)
        except Exception as e:
            print(e)
        else:
            self.sesion.add(self.charla_actual)




    def estado_servicio(self, mensaje):
        pass




    def finalizar_charla(self, mensaje):
        return
        # ??????????? tendria que obener la charla actual nuevamente???
        self.charla_actual.finalizar_charla(mensaje)
        self.CATALOGO_CHARLA.actualizar(self.charla_actual)
