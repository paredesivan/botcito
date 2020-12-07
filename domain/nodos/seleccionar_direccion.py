from domain.nodos.nodo import Nodo
from domain.callprocesor_adapter import obtener_direcciones


class SeleccionarDireccion(Nodo):
    def obtener_menu_dinamico(self, charla):
        # return obtener_direcciones(charla.telefono_destino)
        return '1-balcarce 123 2-uruguay 123910'


    def obtener_titulo(self):
        print(self.tags)
        # return self.tags.texto == '#direccionesTitulo'
