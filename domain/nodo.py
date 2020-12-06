from typing import Set
from domain.tag import Tag


class Nodo:
    def __init__(self, orden, id_nodo, id_padre):
        self.orden = orden
        self.hijos = set()  # type: Set[Nodo]
        self.id_nodo = id_nodo
        self.id_padre = id_padre
        self.tags = set()  # type: Set[Tag]




    def armar_menu(self, charla):
        menu = [self.obtener_titulo()]
        for h in self.hijos:
            menu.append(h.obtener_menu_dinamico(charla))
        return menu




    def obtener_menu_dinamico(self, charla):
        pass




    def obtener_titulo(self):
        pass




    def __str__(self):
        return str(self.__dict__)
