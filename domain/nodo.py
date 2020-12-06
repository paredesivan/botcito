class Nodo:
    def __init__(self,  titulo, orden):
        self.orden = orden
        self.titulo = titulo

    def __str__(self):
        return str(self.__dict__)
