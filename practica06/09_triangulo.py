#!/usr/bin/python
#
#   9.- Escribe un programa que calcule la superficie de un triángulo, para ello tiene que pedir la longitud de la base y de la altura:
#       Vamos a calcular la superficie de un triángulo...
#       ¿Cuánto mide de base (en cm): 21
#       ¿Cuánto mide de altura (en cm): 17
#       La superficie del triángulo es de 178.5 cm^2.
#
#   Víctor Manuel Andreu Felipe 2025

base = float(input("¿Cuánto mide de base (en cm): "))
altura = float(input("¿Cuánto mide de altura (en cm): "))

area = base * altura / 2

print("La superficie del triángulo es de", area, "cm^2.")