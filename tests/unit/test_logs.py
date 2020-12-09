import unittest
import domain.log as logs


class MyTestCase(unittest.TestCase):

    def test_something(self):

        logs = [1, 2, [{'hola'},3, 4, 5], 6]
        # realizar tratamiento para que cada log se guarde como si fuera un registro
        salida = []
        for l in logs:
            if not isinstance(l, list):
                salida.append(l)
                continue
            # si es una lista
            for j in l:
                salida.append(j)

        salidanueva = [1, 2, {'hola'},3, 4, 5, 6]

        print(salida)
        self.assertEqual(salida, salidanueva)
