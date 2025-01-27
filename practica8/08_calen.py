#!/usr/bin/python
#
#   8.- Escribir un programa que “dibuje” un mes del calendario. El programa recibirá como entrada el
#   número de días del mes y el día de la semana del primer día del mes. Ejemplo:
#       Número de días del mes: 31
#       Día 1 es (0 lunes, 6 domingo): 4
#       L  M  X  J  V  S  D
#                   1  2  3
#       4  5  6  7  8  9 10
#      11 12 13 14 15 16 17
#      18 19 20 21 22 23 24
#      25 26 27 28 29 30 31
#
#   Victor Manuel Andreu Felipe 2025

# control de errores
num = 0
while num < 1 or num > 31:
    num = int(input("Número de días del mes: "))
    if num < 1 or num > 31:
        print("Error: Un mes tiene entre 1 y 31 días.")

diasem = -1
while diasem < 0 or diasem > 6:
    diasem = int(input("Día 1 es (0 lunes, 6 domingo): "))
    if diasem < 0 or diasem > 6:
        print("Error: Debe ser un número entre 0 y 6.")

# cabecera
print(" L  M  X  J  V  S  D")

fila = ""   # Variable que será la salida por pantalla
            # donde vamos a ir concatenando cosas

for i in range(diasem): # bucle para agregar 3 espacios por cada                        
    fila += "   "       # por cada día de la semana en el que empecemos

cont = diasem           # contador para movernos por la fila

for diasem in range(1, num + 1):
    if diasem < 10:     # si el día de la semana solo tiene una cifra
                        # se imprime un espacio a la izquierda
        fila += " " + str(diasem) + " "
    else:
        fila+= str(diasem) + " "

    cont += 1

    if cont == 7:       # con esto reiniciamos la fila cada domingo
        print(fila)
        cont = 0
        fila = ""

print(fila)
 