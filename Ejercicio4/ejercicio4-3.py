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