from domain.nodos.nodo import Nodo


class IngresarDireccion(Nodo):
    def obtener_menu_dinamico(self, charla):
        return self.tags[0].texto



    def obtener_titulo(self):
        print(self.tags)
        return self.tags[0].texto
