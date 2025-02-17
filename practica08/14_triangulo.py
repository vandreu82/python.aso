#!/usr/bin/python
#
#   14.- Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de
#   la figura.
#       Nivel: 4
#           XX 
#          XXXX
#         XXXXXX
#        XXXXXXXX
#
#       Nivel: 3
#           X
#          XXX
#         XXXXX
#
#       Nivel: 2
#           XX
#          XXXX
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Nivel: "))

# comprobacion de rango
if num < 2 or num > 40:
    print("El número debe estar entre 2 y 40")
else:
    i = 1
    while i <= num:
        espa = num - i  # ajustamos el espaciado inicial
        # imprimimos la línea con espacios y el doble de X por número de línea
        # el espaciado de la derecha no es necesario pues saltamos de línea
        print(" " * espa + "X" * (2 * i))
        i += 1  # pasamos a la siguiente línea