#!/usr/bin/python
#
#   12.- Escribir un programa que solicite un número n y a continuación muestre si el número es o no
#   primo. Ejemplos:
#       Introduzca un número: 100
#       El número no es primo
#       Introduzca un número: 101
#       El número es primo
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num <= 0:
    print("El número debe ser positivo")
elif num == 1:
    print("El número no es primo")  # excepcion del 1 que no es primo
else:
    i = 2           # empezamos en el 2 porque el 1 no es primo
    corr = ""       
    while i < num:          # bucle que recorre todos los números anteriores
        if num % i == 0:    # dividiéndolo entre ellos buscando divisores
            corr = "no "
            break
        i += 1

    print("El número " + corr + "es primo")