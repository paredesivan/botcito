from typing import Set
from domain.tag import Tag
from adapters.sql_repository_tag import SqlRepositoryTag

class Nodo:
    def __init__(self, orden, id_nodo, id_padre):

        self.orden = orden
        self.id_nodo = id_nodo
        self.id_padre = id_padre


    def procesar(self):
        pass



    def obtener_opciones(self, charla):
        menu = [self.obtener_titulo()]
        for h in self.hijos:
            menu.append(h.obtener_menu_dinamico(charla))
        return menu





    def obtener_titulo(self):
        pass




    def __str__(self):
        return str(self.__dict__)

