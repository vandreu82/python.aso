#!/usr/bin/python
#
#  10.- Escribe un programa que calcule potencias para un número dado. El programa debe pedir un
#   número y a continuación calcular el cuadrado, el cubo, la potencia cuarta y la potencia quinta. En
#   Python se puede calcular el cubo de un número de dos formas:
#       x * x * x
#       x ** 3
#   Ejemplo:
#       Dame un número: 3
#       3 ^ 2 = 9
#       3 ^ 3 = 27
#       3 ^ 4 = 81
#       3 ^ 5 = 243
#
#   Víctor Manuel Andreu Felipe 2025

numero = int(input("Dame un número: "))

print(numero, "^ 2 =", numero ** 2)
print(numero, "^ 3 =", numero ** 3)
print(numero, "^ 4 =", numero ** 4)
print(numero, "^ 5 =", numero ** 5)
