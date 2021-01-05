from service_layer.catalogo_charla import CatalogoCharlas
from service_layer.catalogo_parametro import CatalogoParametros
from single import singleton
from domain.charla import Charla
from domain.excepciones import ElementoVacio
from adapters.sql_repository_log import SqlRepositoryLog
from adapters.sql_repository_nodo import SqlRepositoryNodo
from adapters.sql_repository_tag import SqlRepositoryTag


def es_mensaje_invalido(mensaje):
    return mensaje is None


@singleton
class ControladorBot:
    def __init__(self, sesion):

        self.CATALOGO_CHARLA = CatalogoCharlas(sesion)
        self.CATALOGO_PARAMETROS = CatalogoParametros(sesion)
        self.SQL_REPOSITORY_NODO = SqlRepositoryNodo(sesion)
        self.SQL_REPOSITORY_TAG = SqlRepositoryTag(sesion)
        self.parametro_actual = self.obtener_parametro_actual()
        self.charla_actual = None
        self.sesion = sesion




    def obtener_parametro_actual(self):
        parametro = self.CATALOGO_PARAMETROS.buscar_parametro_activo()
        if parametro == 0:
            raise ElementoVacio("no existe el parametro, no se puede iniciar la charla")
        return parametro




    def existe_charla(self):
        return self.charla_actual is not None and self.charla_actual != 0




    def finalizar_charlas_viejas(self):
        self.CATALOGO_CHARLA.finalizar_charlas_viejas()




    def nuevo_mensaje(self, mensaje):

        if es_mensaje_invalido(mensaje):
            raise ElementoVacio("no hay mensaje")

        # mensaje es una palabra reservada de airtrack
        #       ejecutar accion
        #       salir

        self.charla_actual = self.CATALOGO_CHARLA.buscar_charla_existente(mensaje.get('telefono_origen'))

        if not self.existe_charla():
            self.crear_charla(mensaje)
            self.charla_actual.procesar_nodo()

        log = self.charla_actual.obtener_log(self.charla_actual.id_charla, mensaje['opcion'])

        menu = self.procesar_menu(log)

        self.charla_actual.guardar_logs(menu, self.sesion)

        # hago un solo commit al final para garantizar integridad
        self.sesion.commit()
        self.sesion.close()

        self.ATMSJ_ADAPTER.enviar_menu(menu)

        return {'ok'}


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
        # obtener accion a realizar (no buscar_parametro_activo en la bd porque si la cambio a la bd en tiempo real se rompera)
        # segun el modo determinar a que funcion llamar




    def procesar_menu(self, log):

        if self.es_una_opcion_valida(log):
            # si es una opcion valida
            # self.charla_actual.procesar_nodo(log)
            # no se que hace bien, pero aca deberia ejecutar el comportamiento del nodo
            ultimo_nodo = self.charla_actual.actualizar_ultimo_nodo(log)
            opciones = ultimo_nodo.obtener_opciones(self.charla_actual)
            menu = ultimo_nodo.armar_menu(opciones)
            return menu

        # si no es una opcion valida
        self.charla_actual.incrementar_intentos_fallidos()
        supero_limite_intentos = self.charla_actual.validar_intentos_fallidos(
            self.PARAMETRO.maximo_intentos_fallidos)
        if supero_limite_intentos:
            self.CATALOGO_CHARLA.finalizar_charla(self.charla_actual.id_charla)
            # no guardo los logs, porque es al pedo replicar los registros
            menu = self.SQL_REPOSITORY_TAG.obtener_texto('#intentos_fallidos')
            return menu

        # si no supero el limite de intentos
        opciones = self.charla_actual.obtener_ultimos_logs(self.charla_actual.id_charla)
        menu = self.charla_actual.armar_menu(opciones)
        return menu




    def crear_charla(self, mensaje):
        self.parametro_actual = self.obtener_parametro_actual()

        id_modo_actual = self.parametro_actual.id_modo

        nodo_inicial = self.SQL_REPOSITORY_NODO.obtener_nodo_inicial(id_modo_actual)

        # crea una charla, con el ultimo nodo como el actual
        try:
            self.charla_actual = Charla(telefono_destino=mensaje.get('telefono_destino'),
                                        telefono_origen=mensaje.get('telefono_origen'),
                                        id_modo=self.parametro_actual.id_modo,
                                        ultimo_nodo=nodo_inicial)
        except Exception as e:
            print(e)  # seria mejor lanzarla
        else:
            self.sesion.add(self.charla_actual)





    def estado_servicio(self, mensaje):
        pass




    def finalizar_charla(self):
        self.CATALOGO_CHARLA.actualizar(self.charla_actual.id_charla)
