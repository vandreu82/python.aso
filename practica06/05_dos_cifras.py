#!/usr/bin/python
#
#   5.- Escribir un programa que pida un número de 2 cifras, a continuación debe mostrar el número al revés. Ejemplo:
#       Dame un número: 24
#       El número al revés es: 42
#
#   Víctor Manuel Andreu Felipe 2025

numero = int(input("Dame un número: "))     # convertimos a int para hacer operaciones
decenas = int(numero / 10)                  # convertimos el resultado a int para que no de decimales
unidades = numero % 10

print("El número al revés es: ", unidades, decenas, sep='')