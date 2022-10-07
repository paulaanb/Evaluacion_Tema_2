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