import unittest
from domain.charla import Charla
from domain.nodos.nodo import Nodo


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.charla = Charla(
            ultimo_nodo=Nodo(1, 2, 3, 4),
            id_modo=2,
            telefono_origen='213',
            telefono_destino='2131'
        )




    def test_something(self):
        logs = [1, 2, [{'hola'}, 3, 4, 5], 6]
        salida_deseada = [1, 2, {'hola'}, 3, 4, 5, 6]
        salida_de_la_funcion = self.charla.formatear_logs(logs)
        self.assertEqual(salida_deseada, salida_de_la_funcion)




    def test_something_2(self):
        logs = [1, 2, 3, 4, 5, 6]
        salida_deseada = [1, 2, 3, 4, 5, 6]
        salida_de_la_funcion = self.charla.formatear_logs(logs)
        self.assertEqual(salida_deseada, salida_de_la_funcion)


    def test_something_3(self):
        logs = []
        salida_deseada = []
        salida_de_la_funcion = self.charla.formatear_logs(logs)
        self.assertEqual(salida_deseada, salida_de_la_funcion)
