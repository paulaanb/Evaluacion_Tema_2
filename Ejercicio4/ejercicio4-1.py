#Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añade m mensajes explicativos para el usuario.
#1) Código a evaluar:

numero = 7/0

def division(a, b):
   try:
       result = a / b
     except ZeroDivisionError:
      print('¡No se puede dividir por cero!')
    else:
       print(result)

#Otra forma de error
try:
    resultado = 10/0
except ZeroDivisionError:
    print("ERROR: división por cero")
else:
    print("División realizada correctamente")
finally:
    print("Fin del bloque try")
ERROR: división por cero
Fin del bloque try