from typing import Set
from domain.tag import Tag
from adapters.sql_repository_tag import SqlRepositoryTag


class Nodo:
    def __init__(self, id, orden, id_nodo, id_padre):
        self.orden = orden
        self.id = id
        self.id_nodo = id_nodo
        self.id_padre = id_padre




    def procesar(self):
        pass




    def obtener_opciones(self, charla):
        titulo = self.obtener_titulo()
        menu = [titulo]
        for hijo in self.hijos:
            menu.append(hijo.obtener_menu_dinamico(charla))
        return menu




    def obtener_titulo(self):
        pass




    def obtener_menu_dinamico(self):
        pass




    def __str__(self):
        return str(self.__dict__)
