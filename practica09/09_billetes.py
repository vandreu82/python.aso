#!/usr/bin/python
#   9.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
#   de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
#   Monedas: 2 €, 1 €. El programa debe tener una lista con los billetes y monedas de curso legal.
#   Ejemplo:
#       Introduzca una cantidad: 2343
#       4 billetes de 500
#       1 billete de 200
#       1 billete de 100
#       2 billetes de 20
#       1 moneda de 2
#       1 moneda de 1
#
#   Victor Manuel Andreu Felipe 2025

def calcular_cambio(cantidad):
    # definimos los billetes/monedas
    billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    resultado = []
    
    # iteramos hasta llegar a 1
    for valor in billetes_monedas:
        cantidad_billetes = cantidad // valor  # calculamos la cantidad
        if cantidad_billetes > 0:
            tipo = "billete" if valor >= 5 else "moneda"
            plural = "s" if cantidad_billetes > 1 else ""
            # preparamos la cadena
            resultado.append(f"{cantidad_billetes} {tipo}{plural} de {valor}€") 
            cantidad %= valor  # actualizamos la cantidad
    
    return resultado

# control de input
while True:
    try:
        cantidad = int(input("Introduzca una cantidad en euros: ").strip())
        if cantidad >= 0:
            break
        else:
            print("Por favor, introduce una cantidad positiva.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

cambio = calcular_cambio(cantidad)
for linea in cambio:
    print(linea)
