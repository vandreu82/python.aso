#!/usr/bin/python
#
#    9.- Escribir un programa que pida cuatro números enteros por teclado y determine el mayor y el
#    menor de los cuatro números. Ejemplo:
#       Introduzca 4 números enteros: 20 34 10 -18
#       Mayor número: 34
#       Menor número: -18
#
#   Victor Manuel Andreu Felipe 2025

cadena = str(input("Introduzca 4 números enteros(separados por espacios): "))

partes = cadena.split(" ")

num1 = int(partes[0])
num2 = int(partes[1])
num3 = int(partes[2])
num4 = int(partes[3])

# calculamos el mayor
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print("Mayor número:", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("Mayor número:", num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("Mayor número:", num3)
else:
    print("Mayor número:", num4)

# calculamos el menor
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    print("Menor número:", num1)
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    print("Menor número:", num2)
elif num3 <= num1 and num3 <= num2 and num3 <= num4:
    print("Menor número:", num3)
else:
    print("Menor número:", num4)