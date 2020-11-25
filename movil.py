class Movil:
    def __init__(self, _id, _patente, chofer):
        self.chofer = chofer
        self.id_movil = _id
        self.patente = _patente




    def obtener_id(self):
        return self.id_movil




    def __eq__(self, other):
        # no se como funciona, pero si no esta no anda el test
        if not isinstance(other, Movil):
            return False
        return other.id_movil == self.id_movil  # devuelve true si es la misma instancia?? creo que si. asi anda el test
    # porque compara dos objetos o compara los id de los 2 objetos???
