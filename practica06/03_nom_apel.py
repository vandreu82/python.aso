#!/usr/bin/python
#
#   3.- Escribe un programa que pregunte por tu nombre, por tu primer apellido y por tu segundo apellido.
#    A continuación imprimirá tu nombre de dos maneras:
#       ¿Cuál es tu nombre? José Antonio
#       ¿Y tu primer apellido? Sánchez
#       ¿Y tu segundo apellido? Pérez
#       Te llamas: José Antonio Sánchez Pérez
#       En las listas aparecerías como: Sánchez Pérez, José Antonio
#
#   Víctor Manuel Andreu Felipe 2025

nombre = input("¿Cuál es tu nombre? ")
apel1 = input("¿Y tu primer apellido? ")
apel2 = input("¿Y tu segundo apellido? ")

print("Te llamas:", nombre, apel1, apel2)
print("En las listas aparecerías como:", apel1, apel2, nombre)