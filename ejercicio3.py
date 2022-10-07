#Creamos la clase porducto que tenga los atributos codigo, nombre, precio y tipo
class Producto:
 
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
 
    def __str__(self):
        return """\

codigo\t{}
nombre\t\t{}
precio\t\t{}
tipo\t{}""".format(self.codigo, self.nombre, self.precio, self.tipo)
 
 
@property
 def codigo(self):
 
    return self.__codigo
 
@codigo.setter
 def codigo(self, nuevoValor):
 
    self.__codigo = nuevoValor
 
@property
 def nombre(self):
 
    return self.__nombre
 
@nombre.setter
 def nombre(self, nuevoValor):
 
    self.__nombre = nuevoValor
 
@property
 def precio(self):
 
    return self.__precio
 
@precio.setter
 def precio(self, nuevoValor):
 
    self.__precio = nuevoValor
 
@property
 def tipo(self):
 
    return self.__tipo
 
@tipo.setter
 def tipo(self, nuevoValor):
 
    self.__tipo = nuevoValor

#Creamos el constructor de la clase con print para comprobar que el producto se haya creado con exito
p1= (12, "leche", 1, "lacteo")
p2= (10, "pollo", 4, "carne")
print("\nProbando el producto con un print:")
print(p1)
print(p2)