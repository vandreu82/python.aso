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
#   Como no se pueden usar listas, no conozco la forma de pedir la fecha en DD/MM/YY y luego dividirla

dia = int(input("Introduzca el día del mes: "))
mes = int(input("Introduzca el mes en número: "))
ano = int(input("Introduzca el año: "))

# comprobamos que los meses y los días esten correctos

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 0 or dia > 31:
        corr = "incorrecta"
    else:
        corr = "correcta"
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 0 or dia > 30:
        corr = "incorrecta"
    else:
        corr = "correcta"
# comprobamos los años bisiestos (tengo una duda, 
# ¿un año negativo(antes de cristo) puede ser bisiesto?)
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 0 or dia > 29:
            corr = "incorrecta"
        else:
            corr = "correcta"
    else: 
        if dia <= 0 or dia > 28:
            corr = "incorrecta"
        else:
            corr = "correcta"
else:   # aqui comprobamos que los meses estén entre 1 y 12
    corr = "incorrecta"

# asignación de nombre a los meses numéricos

if mes == 1:
    mes = "Enero"
elif mes == 2:
    mes = "Febrero"
elif mes == 3:
    mes = "Marzo"
elif mes == 4:
    mes = "Abril"
elif mes == 5:
    mes = "Mayo"
elif mes == 6:
    mes = "Junio"
elif mes == 7:
    mes = "Julio"
elif mes == 8:
    mes = "Agosto"
elif mes == 9:
    mes = "Septiembre"
elif mes == 10:
    mes = "Octubre"
elif mes == 11:
    mes = "Noviembre"
elif mes == 12:
    mes = "Diciembre"

if corr == "correcta":
    print("La fecha es " + str(dia) + " de " + str(mes) + " de " + str(ano))
else:
    print("La fecha es", corr)