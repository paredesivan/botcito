from domain.excepciones import IntentosFallidosException, CharlaInactiva


class Charla:
    def __init__(self,  estado, intentos_fallidos, telefono_destino, telefono_origen, usuario_responsable):
        self.estado = estado
        self.intentos_fallidos = intentos_fallidos
        self.telefono_destino = telefono_destino
        self.telefono_origen = telefono_origen
        self.usuario_responsable = usuario_responsable




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
