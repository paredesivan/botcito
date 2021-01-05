from adapters.sql_repository import SqlRepository
from domain.parametro import Parametro

from single import singleton
@singleton
class SqlRepositoryParametro(SqlRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, charla):
        self.session.add(charla)




    def get(self,id_sucursal):
        resultado = self.session.query(Parametro)
        if resultado is None:
            return 0
        return resultado.first()





# class SqlAlchemyRepository(AbstractRepository):
#
#     def __init__(self, session):
#         super().__init__()
#         self.session = session
#
#     def _add(self, product):
#         self.session.add(product)
#
#     def _get(self, sku):
#         return self.session.query(model.Product).filter_by(sku=sku).first()
#
#     def _get_by_batchref(self, batchref):
#         return self.session.query(model.Product).join(model.Batch).filter(
#             orm.batches.c.reference == batchref,
#         ).first()
