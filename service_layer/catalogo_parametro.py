from domain.excepciones import ElementNotFoundException, ErrorAlActualizar
from adapters.sql_repository_parametro import SqlRepositoryParametro
from single import singleton


@singleton
class CatalogoParametros:

    def __init__(self, sesion):
        self.sesion = sesion

    def buscar(self):
        resultado = SqlRepositoryParametro(self.sesion).get(None)
        if resultado != 0:
            return resultado
        return 0

