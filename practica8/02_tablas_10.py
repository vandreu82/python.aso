#!/usr/bin/python
#
#   2.- Escribir un programa que imprima las 10 tablas de multiplicar.
#
#   Victor Manuel Andreu Felipe 2025

for i in range(0, 11):
    print("")   # separador
    for j in range (0, 11):
        print(i, "x",j, "=", i * j)