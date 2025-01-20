#!/usr/bin/python
#
#   5.- Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Escribir un programa
#   que calcule el sueldo bruto mensual en euros a partir de los siguientes datos:
#       • Días trabajados.
#       • Días festivos trabajados.
#       • Turno: mañana, tarde, noche.
#   ... con las siguientes restricciones:
#       • Un día tiene 8 horas laborales.
#       • Las horas de un día normal se pagan a 12 €, las horas de un día festivo se pagan a 24€.
#       • Un trabajador en un mes, sólo puede trabajar en un turno y 8 horas al día.
#       • Los meses son de 30 días.
#       • El turno de noche se paga un 20% más que los turnos de mañana y tarde.
#   Ejemplo:
#       Días trabajados: 22
#       Días festivos trabajados: 5
#       Turno (M-mañana, T-tarde, N-noche): M
#       Sueldo: 3072 euros
#
#   Victor Manuel Andreu Felipe 2025

dlab = int(input("Días trabajados: "))
dfest = int(input("Días festivos trabajados: "))
turno = str(input("Turno (M-mañana, T-tarde, N-noche): "))

# primero controlamos las restricciones de horas y días

if dlab < 0 or dfest < 0:
    print("No se pueden trabajar horas negativas")
elif dlab == 0 and dfest == 0:
    print("Esta persona no ha trabajado con nosotros")
elif dlab + dfest > 30:
    print("No hay tantos días en un mes")
else:
    # y luego controlamos el turno
    if turno == 'N':
        sueldo = dlab * 8 * 12 * 1.2 + dfest * 8 * 24 * 1.2
        print("Sueldo:", sueldo, "euros")
    elif turno == 'M' or turno == 'T':
        sueldo = dlab * 8 * 12 + dfest * 8 * 24
        print("Sueldo:", sueldo, "euros")
    else:
        print("Ese turno no existe")