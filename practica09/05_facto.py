#!/usr/bin/python
#
#   5.- Escribir un programa que pida un número entre 0 y 400, a continuación debe calcular todos
#   los factoriales entre el cero y el número solicitado. El programa debe tener una función factorial
#   que realice el cálculo. Ejemplo:
#       Introduce un número: 5
#       0! = 1
#       1! = 1
#       2! = 2
#       3! = 6
#       4! = 24
#       5! = 120
#
#   Victor Manuel Andreu Felipe 2025

# cálculo del factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# iteración para mostrar los factoriales
def show_factos(tope):
    for i in range(tope + 1):
        print(f"{i}! = {factorial(i)}")

while True:
    # control de input
    try:
        numero = int(input("Introduce un número entre 0 y 400: "))
        if 0 <= numero <= 400:
            break
        else:
            print("Por favor, introduce un número en el rango válido (0-400).")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

show_factos(numero)
