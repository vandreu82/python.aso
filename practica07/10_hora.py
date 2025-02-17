#!/usr/bin/python
#
#    10.- Escribe un programa que dada una hora en el formato hh:mm:ss muestre la hora siguiente.
#    Ejemplo:
#       Hora: 23:58:59
#       23:59:00
#    Ejemplo:
#       Hora: 23:63:59
#       La hora es incorrecta
#
#   Victor Manuel Andreu Felipe 2025
#
# Como no se pueden usar listas, no se recoger la hora en hh:mm:ss

hour = int(input("Hora: "))
min = int(input("Minutos: "))
sec = int(input("Segundos: "))
if (hour < 0 or hour > 23 or
    min < 0 or min > 59 or
    sec < 0 or sec > 59):
    print("La hora es incorrecta")
else:   # incrementamos la hora en 1 segundo
    sec += 1
    if sec == 60:   # comprobamos los valores tope y reseteamos en caso necesario
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if hour == 24:
        hour = 0
 
    hourlit = str(hour)
    # si los valores son menor que 10, agregamos un 0 la izquierda
    if min < 10:
        minlit = "0" + str(min)
    else:
        minlit = str(min)
    if sec < 10:
        seclit = "0" + str(sec)
    else:
        seclit = str(sec)
    print(hourlit + ":" + minlit + ":" + seclit)