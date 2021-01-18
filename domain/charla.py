from domain.excepciones import IntentosFallidosException, CharlaInactiva
from adapters.sql_repository_log import SqlRepositoryLog


class Charla:
    def __init__(self,
                 ultimo_nodo,
                 id_modo,
                 telefono_destino,
                 telefono_origen,
                 estado='activa',
                 intentos_fallidos=0,
                 usuario_responsable='automatico',
                 datos=None):
        # print(ultimo_nodo)

        self.id_modo = id_modo
        self.estado = estado
        self.intentos_fallidos = intentos_fallidos
        self.telefono_destino = telefono_destino
        self.telefono_origen = telefono_origen
        self.camello = 'sasaa'  # puesta a modo de prueba para que se vea que no lo agrega a la bd, porque no esta enlazada
        self.usuario_responsable = usuario_responsable
        self.datos = datos
        self.logs = list()
        self.ultimo_nodo = ultimo_nodo
        self.id_ultimo_nodo = ultimo_nodo.id  # solo para la base de datos




    def obtener_arbol(self):
        return self.modo.arbol




    # def crear_log(self):
    #     log=Log()

    def esta_charla_activa(self):
        if self.estado != 'activa':
            raise CharlaInactiva()
        return True




    def obtener_estado(self):
        return self.estado




    def obtener_intentos_fallidos(self):
        return self.intentos_fallidos




    def incrementar_intentos_fallidos(self):
        self.intentos_fallidos += 1




    def validar_intentos_fallidos(self, maximo_intentos_fallidos):
        return maximo_intentos_fallidos <= self.intentos_fallidos




    def guardar_logs(self, logs, sesion):

        lista_logs = self.formatear_logs(logs)

        # crear los logs
        return SqlRepositoryLog(sesion).add(lista_logs)




    def setear_ultimo_nodo(self, nodo):
        self.ultimo_nodo = nodo




    def formatear_logs(self, logs):
        lista_logs = []
        for log in logs:
            if not isinstance(log, list):
                lista_logs.append(log)
                continue
            # si es una lista
            for j in log:
                lista_logs.append(j)
        return lista_logs




    def set_estado(self,estado):
        self.estado = estado




    def __repr__(self):
        return str(self.__dict__)




    def __str__(self):
        return str(self.__dict__)
