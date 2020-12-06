from domain.nodo import Nodo
from domain.callprocesor_adapter import obtener_direcciones


class SeleccionarDireccion(Nodo):
    def obtener_menu(self, charla):
        return obtener_direcciones(charla.telefono_destino)
