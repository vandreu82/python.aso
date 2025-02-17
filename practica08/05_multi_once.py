#!/usr/bin/python
#
#   5.- Escribe un programa que dado un número, muestre todos los múltiplos de 11 desde el cero
#   hasta el número.
#       Introduzca un número: 125
#       Los múltiplos son: 0 , 11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 , 99 ,
#       110 , 121
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    i = 0
    multi = ""  # cadena para guardar los múltiplos

    while i <= num:
        if multi == "":     # si está vacia(iteración inicial), no 
            multi = str(i)  # imprimimos coma
        else:
            multi = multi + " , " + str(i)
        i += 11             # iteramos de 11 en 11
    
    print("Los múltiplos son:", multi)