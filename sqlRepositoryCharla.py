import sqlalchemy
from fakeRepository import FakeRepository


class SqlRepositoryCharla(FakeRepository):

    def __init__(self):
        pass

    def buscar(self, id_charla):
        return id_charla

    def actualizar(self,charla):
        # actualizar en la bd
        return True
