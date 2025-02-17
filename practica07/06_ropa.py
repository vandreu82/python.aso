#!/usr/bin/python
#
#   6.- Una tienda que vende ropa está de rebajas. La tienda ofrece un 10% de descuento para
#   compras por un importe por debajo de los 20€. Para compras de 20€ en adelante el descuento es
#   del 20%. Escribe un programa que dada la cantidad total de la compra aplique el descuento
#   correctamente y muestra la cantidad final.
#   Ejemplo:
#       Importe total: 18
#       Descuento: 1.8 € (10%)
#       Importe tras descuento: 16.2 €
#   Ejemplo:
#       Importe total: 34
#       Descuento: 6.8 € (20%)
#       Importe tras descuento: 27.2 €
#
#   Victor Manuel Andreu Felipe 2025

pago = float(input("Importe total: "))

if pago <= 0:
    print("Importe incorrecto, debe ser superior a 0 €")
elif pago < 20:
    desc = pago * 0.1
    print("Descuento:", desc, "€")
    print("Importe tras descuento:", pago - desc)
else:
    desc = pago * 0.2
    print("Descuento", desc, "€")
    print("Importe tras descuento:", pago - desc)