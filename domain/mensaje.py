class Mensaje:

    # id             texto                                              textousuario    modo
    # # [_saludo,    buenos #hora bienvenido a #empresa,                 saludo           1
    # # [_saludo,    buenos #hora te damos la bienvenida  a #empresa,    saludo2          2

    def __init__(self, id_mensaje, texto, texto_para_cliente):
        self.id_mensaje = id_mensaje
        self.texto = texto
        self.texto_para_cliente = texto_para_cliente




    def obtener_texto(self):
        return self.texto
