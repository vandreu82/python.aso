#!/usr/bin/python
#
#   7.- Escribir un programa que dada una fecha en el formato DIA/MES/AÑO, diga si la fecha es
#   correcta o incorrecta. Si la fecha es correcta el programa debe escribirla con el formato DIA de
#   MES de AÑO.
#   Ejemplo:
#       Introduzca una fecha: 24/12/2004
#       La fecha es 24 de diciembre de 2004
#   Ejemplo:
#       Introduzca una fecha: 31/02/2003
#       La fecha es incorrecta
#   Nota: hay que controlar los años bisiestos, según Wikipedia:
#   "Un año es bisiesto si es divisible entre 4, a menos que sea divisible entre 100. Sin
#   embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta
#   bisiesto. Obviamente, esto elimina los años finiseculares (últimos de cada siglo, que ha de
#   terminar en 00) divisibles solo entre 4 y entre 100.”
#   Dicho de otra forma, un año es bisiesto si:
#   “(si es divisible por 4 Y no es divisible por 100) O es divisible por 400.
#
#   Victor Manuel Andreu Felipe 2025
#   

fecha = str(input("Introduzca una fecha(formato DD/MM/YY): "))

partes = fecha.split("/")   # separamos la fecha

# comprobamos que el formato sea correcto

if len(partes) != 3:
    print("Fecha incorrecta, por favor, use el formato DD/MM/YY")
else:
    
    # asignamos a cada parte una variable

    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    # comprobamos que los meses y los días esten correctos

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 0 or dia > 31:
            corr = "incorrecta"
        else:
            corr = "correcta"
    elif mes == 4 or mes == 6 or mes == 7 or mes == 11:
        if dia < 0 or dia > 31:
            corr = "incorrecta"
        else:
            corr = "correcta"
    # comprobamos los años bisiestos (tengo una duda, 
    # ¿un año negativo(antes de cristo) puede ser bisiesto?)
    elif mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia < 0 or dia > 29:
                corr = "incorrecta"
            else:
                corr = "correcta"
        else: 
            if dia < 0 or dia > 28:
                corr = "incorrecta"
            else:
                corr = "correcta"
    else:   # aqui comprobamos que los meses estén entre 1 y 12
        corr = "incorrecta"
    
    print("La fecha " + str(dia) + "/" + str(mes) + "/" + str(ano) + " es " + corr, sep='')