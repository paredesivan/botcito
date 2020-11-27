class Tag:
    def __init__(self, datos):
        self.id = datos['id_tag']
        self.texto = datos['texto']
        self.texto_para_usuario = ['texto_para_usuario']




    def obtener_id(self):
        return self.id




    def obtener_texto(self):
        return self.texto




    def obtener_texto_para_usuario(self):
        return self.texto_para_usuario
