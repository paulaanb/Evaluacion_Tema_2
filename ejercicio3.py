#Creamos la clase porducto que tenga los atributos codigo, nombre, precio y tipo
class Producto:
 
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
 
    def __str__(self):
        return """\
