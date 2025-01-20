#!/usr/bin/python
#
#   3.- Escribe un programa que dada una nota numérica entre 0 y 10 con dos decimales, diga la
#   nota literal que tiene el alumno. Suponiendo:
#       Sobresaliente: nota en el intervalo [9, 10]
#       Notable: nota en el intervalo [7, 9)
#       Bien: nota en el intervalo [6, 7)
#       Suficiente: nota en el intervalo [5, 6)
#       Suspenso: nota en el intervalo [0, 5)
#       Introduzca la nota: 8.35
#       Nota: Notable
#
#   Victor Manuel Andreu Felipe 2025

nota = float(input("Introduzca la nota: "))

literal = ""

if nota < 5:
    literal = 'Insuficiente'
elif nota >= 5 and nota < 6:
    literal = 'Suficiente'
elif nota >= 6 and nota < 7:
    literal = 'Bien'
elif nota >= 7 and nota < 9:
    literal = 'Notable'
elif nota >= 9:
    literal = 'Sobresaliente'

print("Nota: ", literal)