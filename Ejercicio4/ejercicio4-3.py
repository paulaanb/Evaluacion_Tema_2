#3) Código a evaluar:

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

paises["alemania"]

    def error_index(pais):
        if pais != str:
            print('Introduce el nombre del país entre comillas dobles ("") o simples ('').\nNo se aceptan caracteres difrente a letras.')
        else:
            if pais in paises:
                indice = paises.index(pais)
                return indice
            else:
                 print('pais no encontrado')

#El error que sale si el pais no esta en la lista es el siguiente:
Traceback (most recent call last):
  File "<ejercicio4-3>", line 5, in <module>
    error_index(alemania)
NameError: name 'alemania' is not defined

#Otra forma de error
try:
   paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
   paises["alemania"]
except KeyError:
    print("ERROR: acceso a clave incorrecta en diccionario")
else:
    print("Manejo de diccionario correcto")
finally:
    print("Fin del bloque try")


ERROR: acceso a clave incorrecta en diccionario
Fin del bloque try