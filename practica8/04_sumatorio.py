#!/usr/bin/python
#
#   4.- Escribir un programa que solicite un número positivo, acto seguido debe calcular la suma de
#   todos los números pares comprendidos entre 0 y el numero solicitado. Ejemplo:
#       Introduzca un número: 341
#       La suma es: 29070
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    suma = 0
    i = 0
    while i <= num:
        suma = suma + i
        i += 2  # acumulación para sumar solo los pares

    print("La suma es:", suma)