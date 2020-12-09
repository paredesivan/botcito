from adapters.sql_repository import AbstractRepository
from domain.log import Log
from single import singleton


@singleton
class SqlRepositoryLog(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, log):
        self.session.add(log)




    def get(self, id_log):
        return self.session.query(Log).filter_by(id_log=id_log).first()




    def obtener_log(self, id_charla, opcion):
        return self.session.query(Log) \
            .filter_by(opcion=opcion,
                       id_charla=id_charla,
                       estado='activo') \
            .first()
