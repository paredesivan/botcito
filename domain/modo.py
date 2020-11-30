
class Modo():
    def __init__(self, id_modo,  nombre):
        self.id_modo = id_modo
        self.nombre = nombre

    def __repr__(self):
        return "modo(" \
               "id_modo={self.id_modo}," \
               "nombre={self.nombre}".format(self=self)

