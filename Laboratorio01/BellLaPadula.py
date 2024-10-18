class Usuario:
    def __init__(self, nombre, nivel_de_seguridad):
        self.nombre = nombre
        self.nivel_de_seguridad = nivel_de_seguridad

class Documento:
    def __init__(self, nombre, clasificacion):
        self.nombre = nombre
        self.clasificacion = clasificacion

class BellLaPadula:
    def puede_leer(self, usuario, documento):
        
        if usuario.nivel_de_seguridad >= documento.clasificacion:
            return f"{usuario.nombre} puede leer {documento.nombre}"
        else:
            return f"{usuario.nombre} no puede leer {documento.nombre}"

    def puede_escribir(self, usuario, documento):
        
        if usuario.nivel_de_seguridad <= documento.clasificacion:
            return f"{usuario.nombre} puede escribir en {documento.nombre}"
        else:
            return f"{usuario.nombre} no puede escribir en {documento.nombre}"


documentos = [
    Documento("Documento Confidencial", 2),
    Documento("Top Secret", 3),
    Documento("Documento Público", 1)
]


usuarioblp1 = Usuario("UsuarioBellLaPadula1", 3)


blp = BellLaPadula()


for doc in documentos:
    print(blp.puede_leer(usuarioblp1, doc))
    print(blp.puede_escribir(usuarioblp1, doc))
