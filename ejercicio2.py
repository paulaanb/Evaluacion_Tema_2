#Copiamos el ejercicio 1 como indica el enunciado
#Creamos la clase Alumno que tenga los atributos nombre y nota
class Alumno:

    def inicio(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
#Constructor de clase
    def constructor(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def calificacion(self):
        if self.nota>=4:
            print("Aprobado")
        else:
            print("Suspenso")


# Bloque de experimentacion donde ponemos los ejemplos

alumno1=Alumno()
alumno1.inicio"Paula",2)
alumno1.constructor()
alumno1.calificacion()

alumno2=Alumno()
alumno2.inicio("Ruben",10)
alumno2.constructorr()
alumno2.calificacion()

def __str__(self): return "Lo que quiero mostrar"

class alumno:
    def __init__(self,nom,no):
        self.nombre=nom
        self.nota=no

    def __str__(self):
        cadena=self.nombre+","+self.nota
        return cadena


#Bloque experimental donde ponemos los ejemplos
 
alumno1=Alumno("Paula","2")
alumno2=Alumno("Ruben","10")
print(str(alumno1)+"-"+str(alumno2))  
# La solucion que va a salir es la siguiente: Paula, 2- Ruben, 10