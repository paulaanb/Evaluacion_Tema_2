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

