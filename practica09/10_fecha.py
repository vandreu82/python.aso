#!/usr/bin/python
#
#   10.- Escribe una función que dado el día, el mes y el año, devuelva un entero comprendido entre
#   1 y 366 indicando el número de día del año. La función tendrá esta declaración:
#      dia_agno(dia, mes, agno)
#
#   Victor Manuel Andreu Felipe 2025

# primero comprobamos si el año es bisiesto
def es_bisiesto(agno):
    return (agno % 4 == 0 and agno % 100 != 0) or (agno % 400 == 0)

def dia_agno(dia, mes, agno):
    # definimos los días de cada mes
    dias_por_mes = [31, 29 if es_bisiesto(agno) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # comprobación de fecha
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_por_mes[mes - 1]:
        raise ValueError("Fecha incorrecta")
    
    return sum(dias_por_mes[:mes - 1]) + dia


dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
agno = int(input("Introduce el año: "))

try:
    resultado = dia_agno(dia, mes, agno)
    print(f"El día {dia}/{mes}/{agno} corresponde al día {resultado} del año.")
except ValueError as e:
    print(e)
