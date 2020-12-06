from domain.nodo import Nodo
from domain.callprocesor_adapter import obtener_direcciones


class SeleccionarDireccion(Nodo):
    def obtener_menu_dinamico(self, charla):
        return obtener_direcciones(charla.telefono_destino)



    def obtener_titulo(self):
        return self.tags.texto == '#direccionesTitulo'
