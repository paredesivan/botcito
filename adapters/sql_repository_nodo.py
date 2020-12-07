from adapters.repository import AbstractRepository
from domain.nodos.nodo import Nodo
from single import singleton


@singleton
class SqlRepositoryNodo(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def obtener_nodo_inicial(self, id_modo):
        salida = self.session.query(Nodo).filter_by(id_padre=None, id_modo=id_modo)
        salida = salida.first()
        return salida




    def add(self, nodo):
        self.session.add(nodo)




    def get(self, id_tag):
        return self.session.query(Nodo).filter_by(id=id_tag).first()




    def obtener_tags(self, id):
        return self.session.query(Nodo).filter_by(id=id).all()
