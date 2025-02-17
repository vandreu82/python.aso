#!/usr/bin/python
#
#   11.- Escribe un programa que calcule la longitud de una circunferencia. El programa debe pedir el
#   radio y a continuación calcular la longitud. Podemos tomar el valor de pi desde el módulo
#   (librería ) math. Así:
#   import math
#   ...
#       print(math.pi)
#   Ejemplo:
#       Dame el radio (en cm por favor): 3
#       La longitud de la O es: 18.8495559215 cm
#
#   Víctor Manuel Andreu Felipe 2025

import math

radio = float(input("Dame el radio (en cm por favor): "))

circun = 2 * math.pi * radio

print("La longitud de la O es:", circun, "cm")