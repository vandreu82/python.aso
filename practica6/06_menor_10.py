#!/usr/bin/python
#
#   6.- Mejora el programa para que no acepte ni números menores de 10 ni mayores de 99.
#       Ejemplo:
#           Dame un número: 8
#           El número 8 no me sirve, tiene que ser mayor o igual que 10.
#
#   Víctor Manuel Andreu Felipe 2025
#
#   No he sido capaz de hacerlo sin condicionales. Suponiendo que sabemos usar condicionales, el código quedaría así:

numero = int(input("Dame un número: "))     # convertimos a int para hacer operaciones

if numero < 10 or numero > 99:
    print("El número", numero, "no me sirve, tiene que ser mayor o igual que y menor o igual que 99")
else:
    decenas = int(numero / 10)                  # convertimos el resultado a int para que no de decimales
    unidades = numero % 10

    print("El número al revés es: ", unidades, decenas, sep='')