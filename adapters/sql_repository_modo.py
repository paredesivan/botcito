from adapters.sql_repository import SqlRepository
from domain.modo import Modo
from single import singleton

@singleton
class SqlRepositoryModo(SqlRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    # no voy a dejar que se agreguen modos
    def add(self, modo):
        self.session.add(modo)




    def get(self, id_modo):
        return self.session.query(Modo).filter_by(id_modo=id_modo).first()






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
