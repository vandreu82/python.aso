#!/usr/bin/python
#
#   1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número. Hacer el
#   ejercicio de dos formas, con bucle while y con bucle for.
#       Número: 8
#       8 x 0 = 0
#       8 x 1 = 8
#       8 x 2 = 16
#       8 x 3 = 24
#       8 x 4 = 32
#       8 x 5 = 40
#       8 x 6 = 48
#       8 x 7 = 56
#       8 x 8 = 64
#       8 x 9 = 72
#       8 x 10 = 80
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Número: "))

for i in range(0, 11):
    print(num, "x",i, "=", num * i)