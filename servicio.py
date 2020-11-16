class Servicio:
    def __init__(self, datos):
        self.id = datos['id']
        self.datos = datos
    def obtener_id(self):
        return self.id
