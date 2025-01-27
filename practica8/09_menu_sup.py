#!/usr/bin/python
#
#   9.- Escribir un programa para calcular superficies. Constará de un menú que solicitará la figura a
#   la que se va a calcular la superficie, pedirá los datos (lado, base y altura, radio ...) según la figura
#   de la que se trate y visualizará el resultado. El programa deberá calcular superficies de las
#   siguientes figuras: cuadrados, triángulos y círculos. Ejemplo:
#       Cálculo de superficies:
#       1.- Cuadrados
#       2.- Triángulos
#       3.- Círculos
#       4.- Salir
#       Elija opción (1-4): 1
#       Lado: 8
#       La superficie es de 64 cm²
#       (mostramos de nuevo el menú...)
#
#   Victor Manuel Andreu Felipe 2025

while True:         # el bucle se ejecuta siempre, solo salimos con '4'
    print("Cálculo de superficies:")
    print("1.- Cuadrados")
    print("2.- Triángulos")
    print("3.- Círculos")
    print("4.- Salir")
    opcion = input("Introduzca un número: ")
    print()     # linea para presentación

    if (opcion == '4'):
        print("Adios")  
        exit(0)

    if opcion == '1':
        lado = float(input("Lado: "))
        print("La superficie es de: ", lado ** 2, "cm²")

    elif opcion == '2':
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("La superficie es de: ", base * altura / 2, "cm²")

    elif opcion == '3':
        radio = float(input("Radio: "))
        print("La superficie es de: ", 3.1416 * radio ** 2, "cm²")
    
    # control de errores
    else: print("Opción inválida. Introduzca un número entre 1 y 4.")

    print() # linea para presentacion