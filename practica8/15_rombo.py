#!/usr/bin/python
#
#   15.- Escribir un programa que dándole un número (entre 2 y 40) imprima un rombo como el de la
#   figura. Ejemplo:
#       num: 4
#       XXXXXXXX
#       XXX  XXX
#       XX    XX
#       X      X
#       X      X
#       XX    XX
#       XXX  XXX
#       XXXXXXXX
#
#   Victor Manuel Andreu Felipe 2025
# Este programa es parecido al anterior pero se imprime al revés y en fases.
# Y aquí si hay que tener en cuenta el lado derecho.

num = int(input("Nivel: "))

# comprobacion de rango
if num < 2 or num > 40:
    print("El número debe estar entre 2 y 40")
else:
    i = 0  
    while i < num:     # imprimimos la primera mitad
        print("X" * (num - i) + " " * (2 * i) + "X" * (num - i))
        i += 1

    i = num - 1        # y la segunda mitad la imprimimos al revés
    while i >= 0:
        print("X" * (num - i) + " " * (2 * i) + "X" * (num - i))
        i -= 1
