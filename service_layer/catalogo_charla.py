from domain.excepciones import ElementNotFoundException, ErrorAlActualizar
from adapters.sql_repository_charla import SqlRepositoryCharla
from single import singleton


@singleton
class CatalogoCharlas:

    def __init__(self, sesion):
        self.SQL_REPOSITORY_CHARLAS = SqlRepositoryCharla(sesion)
        pass




    def buscar_charla_existente(self, telefono):
        return self.SQL_REPOSITORY_CHARLAS.buscar_charla_existente(telefono)




    def finalizar_charlas_viejas(self):
        return self.SQL_REPOSITORY_CHARLAS.finalizar_charlas_viejas()


    def finalizar_charla(self,id_charla):
        return self.SQL_REPOSITORY_CHARLAS.finalizar_charla(id_charla)
