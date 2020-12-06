from domain.nodo import Nodo
from domain.callprocesor_adapter import obtener_direcciones


class IngresarDireccion(Nodo):
    def obtener_menu_dinamico(self, charla):
        return self.tags.texto == '#direccionesTitulo'



    def obtener_titulo(self):
        return self.tags.texto == '#direcciones'
