from typing import Set

from domain.excepciones import IntentosFallidosException, CharlaInactiva
from domain.log import Log


class Charla:
    def __init__(self,  id_modo,telefono_destino, telefono_origen,estado='activa', intentos_fallidos=0, usuario_responsable='automatico',
                 datos=None):
        self.id_modo = id_modo
        self.estado = estado
        self.intentos_fallidos = intentos_fallidos
        self.telefono_destino = telefono_destino
        self.telefono_origen = telefono_origen
        self.camello = 'sasaa'  # puesta a modo de prueba para que se vea que no lo agrega a la bd, porque no esta enlazada
        self.usuario_responsable = usuario_responsable
        self.datos = datos
        self.logs=set() # type: Set[Log]




    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)




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
        if maximo_intentos_fallidos <= self.intentos_fallidos:
            raise IntentosFallidosException()
        return True




    def finalizar_charla(self):
        self.estado = "finalizada"
