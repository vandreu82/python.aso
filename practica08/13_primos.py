#!/usr/bin/python
#
#   13.- Escribir un programa que solicite un número n y a continuación imprima todos los números
#   primos comprendidos en el intervalo [2-n]. Ejemplo:
#       Introduzca un número: 100
#       Números primos [2-100]: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97
#
#   Victor Manuel Andreu Felipe 2025
#
#############################   Sin terminar

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num <= 0:
    print("El número debe ser positivo")
elif num == 1:
    print("El número 1 no tiene intervalo de primos")  # excepcion del 1 que no es primo
else:
    i = 2           # empezamos en el 2 porque el 1 no es primo
    inter = ""       
    while i <= num:          # bucle que recorre todos los números anteriores
        if num % i == 0:    # dividiéndolo entre ellos buscando divisores
            es_primo = False
        else:
            es_primo = True
        i += 1
        while es_primo == True:
            inter += inter
            
    print("Números primos [2-" + str(num) + "]: " + inter)