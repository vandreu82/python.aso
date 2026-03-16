#!/usr/bin/python
#
#   4.- Escribe un programa que pida nombres. Tras pedirlos debe mostrarlos ordenados.
#   Ejemplo:
#       Introduce nombres. ENTER para terminar
#       luis
#       javier
#       alejandro
#       francisco
#       --pulsamos ENTER--
#       Los nombres son:
#       alejandro
#       francisco
#       javier
#       luis
#
#   Victor Manuel Andreu Felipe 2025

def leer_nombres():
    nombres = []

    print("Introduce nombres. ENTER para terminar")
    while True:
        nombre = input().strip()  # quitamos espacios iniciales y finales

        if nombre == "":  # salida
            break
        
        nombres.append(nombre)  # acumula nombres

    return nombres

def mostrar_nombres_ordenados(nombres):
    print("\nLos nombres son:")
    for nombre in sorted(nombres):  # ordenamos
        print(nombre)

nombres = leer_nombres()
mostrar_nombres_ordenados(nombres)
