#!/usr/bin/python
#
#   6.- Escribir un programa que solicite un número n y a continuación imprima todos los números
#   primos comprendidos en el intervalo [2-n]. El programa debe tener una función es_primo que
#   dado un número devuelva si el número es o no primo. Ejemplo:
#       Introduzca un número: 100
#       Números primos [2-100]: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97
#
#   Victor Manuel Andreu Felipe 2025

# funcion para saber si el número es primo
# usamos solo hasta la raíz cuadrada del número para ahorrar iteraciones
# puesto que al llegar ahí ya se han comprobado los pares
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# muestra todos los numeros primos entre 2 y n
def buscar_primos(n):
    primos = [str(num) for num in range(2, n + 1) if es_primo(num)]
    print(f"Números primos [2-{n}]: {', '.join(primos[:-1])} y {primos[-1]}" if primos else "No hay números primos en el rango.")

# control de input
while True:
    try:
        n = int(input("Introduzca un número: "))
        if n >= 2:
            break
        else:
            print("Por favor, introduce un número mayor o igual a 2.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

buscar_primos(n)
