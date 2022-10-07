#4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

resultado = "2" + 10

try:
    resultado = "2" + 10
except TypeError:
    print("ERROR: intento de suma de número y cadena")
else:
    print("Operación realizada correctamente")
finally:
    print("Fin del bloque try")

ERROR: intento de suma de número y cadena
Fin del bloque try