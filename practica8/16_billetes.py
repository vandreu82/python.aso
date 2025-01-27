#!/usr/bin/python
#
#   16.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
#   de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
#   Monedas: 2 €, 1 €. Ejemplo:
#       Introduzca una cantidad: 2343
#       4 billetes de 500
#       1 billete de 200
#       1 billete de 100
#       2 billetes de 20
#       1 moneda de 2
#       1 moneda de 1
#
#   Victor Manuel Andreu Felipe 2025
#   No me ha dado para hacerlo con bucles :(

num = int(input("Introduzca una cantidad: "))

cont = num

# fracciones
quini = cont // 500
cont %= 500

dosci = cont // 200
cont %= 200

cien = cont // 100
cont %= 100

cincu = cont // 50
cont %= 50

veinte = cont // 20
cont %= 20

diez = cont // 10
cont %= 10

cinco = cont // 5
cont %= 5

dos = cont // 2
cont %= 2

uno = int(cont)

# imprimimos solo las cantidades que no son 0
if quini > 0:
    print(quini, "billetes de 500")
if dosci > 0:
    print(dosci, "billetes de 200")
if cien > 0:
    print(cien, "billetes de 100")
if cincu > 0:
    print(cincu, "billetes de 50")
if veinte > 0:
    print(veinte, "billetes de 20")
if diez > 0:
    print(diez, "billetes de 10")
if cinco > 0:
    print(cinco, "billetes de 5")
if dos > 0:
    print(dos, "monedas de 2")
if uno > 0:
    print(uno, "monedas de 1")
