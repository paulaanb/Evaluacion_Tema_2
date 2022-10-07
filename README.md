# Evaluacion_Tema_2
# Link del repositorio
El link del repowsitorio es el siguiente: Github:[https://github.com/paulaanb/Evaluacion_Tema_2]
# ¿De que trata esta tarea?

# Ejercicio 1
Ejercicio 1 (1 Punto)
Creación (0,5 puntos)
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación (0,5 Puntos)
Crea algunos alumnos

Prueba a ejecutar el método calificacion de cada objeto que has creado

# Ejercicio 2
Ejercicio 2 (1 Punto)
Creación (0,5 puntos)
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:



def __str__(self): return "Lo que quiero mostrar"



Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experimentación (0,5 puntos)
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str

# Ejercicio 3
Ejercicio 3 (1 Punto)
Creación (0,5 Puntos)
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
Experimentación (0,5 Puntos)
Crea algunos productos

Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto

# Ejercicio 4
Ejercicio 4 (2 Punto)
Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añade m mensajes explicativos para el usuario.

Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.



1) Código a evaluar:

numero = 7/0

2) Código a evaluar:

lista = [4, 7, 30, 23, 5]

lista[10]

3) Código a evaluar:

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

paises["alemania"]

4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

resultado = "2" + 10

# Ejercicio 5
Ejercicio 5 (5 puntos)

En este ejercicio vas a trabajar el concepto de herencia un poco más en profundidad, aprovechando para introducir un nuevo concepto muy importante que te facilitará la vida.

Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. Como en el siguiente ejemplo:

Diagrama

Descripción generada automáticamente

class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas

 

    def __str__(self):

        return "Color {}, {} ruedas".format( self.color, self.ruedas )

 

class Coche(Vehiculo):

 

    def __init__(self, color, ruedas, velocidad, cilindrada):

        self.color = color

        self.ruedas = ruedas

        self.velocidad = velocidad

        self.cilindrada = cilindrada

 

    def __str__(self):

        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )

 

 

coche = Coche("azul", 150, 4, 1200)

print(coche)

Color azul, 4 km/h, 150 ruedas, 1200 cc

El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la superclase y luego el específico de la subclase.

Para evitarnos escribir código innecesario, podemos utilizar un truco que consiste en llamar el método de la superclase y luego simplemente escribir el código de la clase:

class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas

 

    def __str__(self):

        return "Color {}, {} ruedas".format( self.color, self.ruedas )

 

 

class Coche(Vehiculo):

 

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

 

    def __str__(self):

        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

 

 

c = Coche("azul", 4, 150, 1200)

print(c)

Color azul, 4 ruedas, 150 km/h, 1200 cc

Como tener que determinar constantemente la superclase puede ser fastidioso, Python nos permite utilizar un acceso directo mucho más cómodo llamado super().

Hacerlo de esta forma además nos permite llamar cómodamente los métodos o atributos de la superclase sin necesidad de especificar el self, pero ojo, sólo se aconseja utilizarlo cuando tenemos una única superclase:

class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas

 

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

 

 

class Coche(Vehiculo):

 

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

 

    def __str__(self):

        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

 

 

c = Coche("azul", 4, 150, 1200)

print(c)

Color azul, 4 km/h, 150 ruedas, 1200 cc

Enunciado

Utilizando esta nueva técnica extiende la clase Vehiculo y realiza la siguiente implementación:

Diagrama

Descripción generada automáticamente

·        Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.

·        Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.

·        Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

Recordatorio

Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto:

type(objeto).__name__