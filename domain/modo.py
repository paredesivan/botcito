from domain.nodos.nodo import Nodo
from typing import  Set


class Modo():
    def __init__(self, id_modo, nombre):
        self.id_modo = id_modo
        self.nombre = nombre
        self.nodos = list()  # type: Set[Nodo]



    def obtener_nodos(self):
        return self.nodos

    def __repr__(self):
        return "modo(" \
               "id_modo={self.id_modo}," \
               "nombre={self.nombre}".format(self=self)


