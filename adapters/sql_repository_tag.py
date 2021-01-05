from adapters.sql_repository import SqlRepository
from domain.tag import Tag
from single import singleton

@singleton
class SqlRepositoryTag(SqlRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, charla):
        self.session.add(charla)




    def get(self, id_tag):
        return self.session.query(Tag).filter_by(id_tag=id_tag).first()




    def obtener_texto(self, id_tag):
        return self.session.query(Tag.texto).filter_by(id_tag=id_tag).first()
