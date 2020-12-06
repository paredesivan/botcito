from domain.nodo import Nodo
from adapters.sql_repository_tag import SqlRepositoryTag


class Saludo(Nodo):



   def obtener_menu_dinamico(self, charla):
      pass





   def obtener_titulo(self):
      return self.tags.texto == '#saludo'

