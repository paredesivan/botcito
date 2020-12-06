from adapters.repository import AbstractRepository
from domain.tag import Tag
from adapters.orm import tabla_tag

class SqlRepositoryTag(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, charla):
        self.session.add(charla)




    def get(self, id_tag):
        return self.session.query(Tag).filter_by(id_tag=id_tag).first()




    def obtener_texto(self, id_tag):
        return self.session.query(Tag.texto).filter_by(id_tag=id_tag).first()
