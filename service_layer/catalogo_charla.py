from domain.excepciones import ElementNotFoundException, ErrorAlActualizar
from adapters.sql_repository_charla import SqlRepositoryCharla
from single import singleton


@singleton
class CatalogoCharlas:

    def __init__(self, sesion):

        self.sesion = sesion
        pass




    def buscar_charla_existente(self, telefono):
        return SqlRepositoryCharla(self.sesion).buscar_charla_existente(telefono)





    def buscar(self, mensaje):
        # buscar en la bd o en memoria la charla??????
        try:
            charla = self.sqlrepository.get(mensaje['id_charla'])
        except:
            raise ElementNotFoundException('no hay elemento en la bd')
        else:  # charla es un objeto que se setea
            return charla




    def actualizar(self, charla):
        try:
            self.sqlrepository.actualizar(charla)
        except:
            raise ErrorAlActualizar()
        else:
            return True
