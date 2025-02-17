#!/usr/bin/python
#
#   11.- Escribir un programa que calcule el factorial de un número dado. Ejemplo:
#       Introduce un número: 7
#       7! = 5040
#
#   Victor Manuel Andreu Felipe 2025
#   código reciclado absolutamente del sumatorio de números pares

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    facto = 1
    i = 1
    while i <= num:
        facto =  facto * i
        i += 1

    print(str(num) + "! =", facto)