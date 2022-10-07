#2) Código a evaluar:

lista = [4, 7, 30, 23, 5]

lista[10]
lista[5:5] = [10]
Traceback (most recent call last):
  File "<lista>", line 5, in <module>
    lista[10]
  Index error: list index out of range

#Otra forma de error
except IndexError:
    print("ERROR: acceso a índice incorrecto en lista")
else:
    print("Manejo de listas correcto")
finally:
    print("Fin del bloque try")

ERROR: acceso a índice incorrecto en lista
Fin del bloque try