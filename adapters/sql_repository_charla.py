from adapters.repository import AbstractRepository
from domain.charla import Charla

from single import singleton
@singleton
class SqlRepositoryCharla(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session




    def add(self, charla):
        self.session.add(charla)




    def get(self, id_charla):
        return self.session.query(Charla).filter_by(id_charla=id_charla).first()




    def buscar_charla_existente(self, telefono):
        resultado=self.session.query(Charla).filter_by(telefono_origen=telefono, estado='activa')
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
