#!/usr/bin/python
#
#   1.- Escribir un programa que pida tres números enteros por teclado y determine el mayor y el
#   menor de los tres números. Ejemplo:
#       Introduzca el primer número: 20
#       Introduzca el segundo número: 34
#       Introduzca el tercer número: -18
#       Mayor número: 34
#       Menor número: -18
#
#   Victor Manuel Andreu Felipe 2025

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

# calculamos el mayor
# Consultar a Alejandro sobre si es mejor
# almacenar en variables y luego imprimir o ir imprimiendo
# y si es necesario recoger el caso de que sean los 3 iguales
# puesto que todos son el mayor y el menor

if num1 >= num2 and num1 >= num3:
#    mayor = num1
    print("Mayor número: ", num1)
elif num2 >= num1 and num2 >= num3:
#    mayor = num2
    print("Mayor número: ", num2)
else:
#    mayor = num3
    print("Mayor número: ", num3)

# calculamos el menor

if num1 <= num2 and num1 <= num3:
#    menor = num1
    print("Mayor número: ", num1)
elif num2 <= num1 and num2 <= num3:
#    menor = num2
    print("Mayor número: ", num2)
else:
#    menor = num3
    print("Menor número: ", num3)

#print("Mayor número: ", mayor)
#print("Menor número: ", menor)
