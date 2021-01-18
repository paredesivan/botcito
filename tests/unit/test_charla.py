import unittest
from domain.charla import Charla
from domain.nodos.nodo import Nodo
from domain.excepciones import CharlaInactiva


class TestCharla(unittest.TestCase):

    def setUp(self):
        self.charla = Charla(
            ultimo_nodo=Nodo(1, 2, 3, 4),
            id_modo=2,
            telefono_origen='213',
            telefono_destino='2131'
        )




    def test_esta_charla_activa_ok(self):
        self.assertEqual(True, self.charla.esta_charla_activa())




    def test_no_esta_charla_activa(self):
        self.charla.set_estado('finalizada')
        # notar que no llama a la funcion, si quiero agregar parametros, van despues de la coma
        # self.assertRaises(CharlaInactiva, self.charla.esta_charla_activa,param1,param2)

        self.assertRaises(CharlaInactiva, self.charla.esta_charla_activa)




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
