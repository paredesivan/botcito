from adapters.repository import AbstractRepository
from domain.nodo import Nodo

class SqlRepositoryNodo(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, charla):
        self.session.add(charla)




    def get(self, id_tag):
        return self.session.query(Nodo).filter_by(id=id_tag).first()




    def obtener_tags(self, id):
        return self.session.query(Nodo).filter_by(id=id).all()
