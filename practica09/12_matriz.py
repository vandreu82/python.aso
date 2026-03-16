#!/usr/bin/python
#
#   12.- Escribe un programa que lea una matriz 5 x 5 de enteros y calcule y muestre la suma de sus
#   filas y de sus columnas:
#       Introduzca fila 1: 2 5 3 4 5
#       Introduzca fila 2: 2 6 8 4 5
#       Introduzca fila 3: 9 8 3 5 2
#       Introduzca fila 4: 5 3 8 5 6
#       Introduzca fila 5: 0 1 4 3 4
#       Totales filas    : 19 25 27 27 12
#       Totales columnas : 18 23 26 21 22
#
#   Victor Manuel Andreu Felipe 2025

def leer_matriz(n):
    """Solicita al usuario ingresar una matriz de tamaño n x n."""
    matriz = []
    for i in range(n):
        while True:
            try:
                fila = list(map(int, input(f"Introduzca fila {i+1}: ").split()))
                if len(fila) == n:
                    matriz.append(fila)
                    break
                else:
                    print(f"Por favor, introduce exactamente {n} números.")
            except ValueError:
                print("Entrada no válida. Introduce números enteros separados por espacios.")
    return matriz

def calcular_sumas(matriz):
    """Calcula y muestra la suma de las filas y las columnas de la matriz."""
    n = len(matriz)
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(n)) for j in range(n)]
    
    print("\nTotales filas :", " ".join(map(str, suma_filas)))
    print("Totales columnas :", " ".join(map(str, suma_columnas)))

# Programa principal
N = 5
matriz = leer_matriz(N)
calcular_sumas(matriz)