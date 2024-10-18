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
        # Un usuario puede leer un documento si su nivel de seguridad es mayor o igual
        if usuario.nivel_de_seguridad >= documento.clasificacion:
            return f"{usuario.nombre} puede leer {documento.nombre}"
        else:
            return f"{usuario.nombre} no puede leer {documento.nombre}"

    def puede_escribir(self, usuario, documento):
        # Un usuario puede escribir en un documento si su nivel de seguridad es menor o igual
        if usuario.nivel_de_seguridad <= documento.clasificacion:
            return f"{usuario.nombre} puede escribir en {documento.nombre}"
        else:
            return f"{usuario.nombre} no puede escribir en {documento.nombre}"

# Crear lista de documentos
documentos = [
    Documento("Documento Confidencial", 2),
    Documento("Top Secret", 3),
    Documento("Documento Público", 1)
]

# Crear un usuario con nivel de seguridad 3
usuarioblp1 = Usuario("UsuarioBellLaPadula1", 3)

# Crear instancia de BellLaPadula
blp = BellLaPadula()

# Verificar acceso de lectura y escritura para cada documento
for doc in documentos:
    print(blp.puede_leer(usuarioblp1, doc))
    print(blp.puede_escribir(usuarioblp1, doc))
