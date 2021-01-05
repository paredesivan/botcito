from domain.nodos.nodo import Nodo
from domain.callprocesor_adapter import obtener_direcciones


class DireccionMapa(Nodo):
    def obtener_menu_dinamico(self, charla):
        return obtener_direcciones(charla.telefono_destino)



    def obtener_titulo(self):
        print(self.tags)

