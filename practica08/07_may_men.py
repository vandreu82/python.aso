#!/usr/bin/python
#
#   7.- Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
#   se introduzca el cero. A continuación debe mostrar el mayor número. Ejemplo:
#       Introduzca un número (cero para terminar): 1230
#       Introduzca un número (cero para terminar): 0.023
#       Introduzca un número (cero para terminar): 12.23
#       Introduzca un número (cero para terminar): 3.1415
#       Introduzca un número (cero para terminar): 280
#       Introduzca un número (cero para terminar): 4234.6
#       Introduzca un número (cero para terminar): 0
#       Mayor: 4234.6
#
#   Victor Manuel Andreu Felipe 2025

num = float(input("Introduzca un número (cero para terminar): "))

if num == 0:
    print("Fin del programa")
else:
    mayor = num 

    while True:
        num = float(input("Introduzca un número (cero para terminar):"))

        if num == 0:
            break

        if num > mayor:
            mayor = num

    print("Mayor:", mayor)
