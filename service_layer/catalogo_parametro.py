from domain.excepciones import ElementNotFoundException, ErrorAlActualizar
from adapters.sql_repository_parametro import SqlRepositoryParametro
from single import singleton


@singleton
class CatalogoParametros:

    def __init__(self, sesion):
        self.sesion = sesion




    def buscar_parametro_activo(self):
        resultado = SqlRepositoryParametro(self.sesion).get(None)
        return resultado if resultado else 0
