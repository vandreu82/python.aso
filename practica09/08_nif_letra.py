#!/usr/bin/python
#
#   8.- Escribe un programa que lea un NIF sin letra por teclado, a continuación debe mostrar el NIF
#   con la letra asociada. El programa debe contar con la función letra_nif que devuelve la letra
#   correspondiente.
#
#   Victor Manuel Andreu Felipe 2025


# calcula la letra del nif
def letra_nif(numero):
    letras_nif = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras_nif[numero % 23]

# control de input
while True:
    try:
        nif_numero = input("Introduce un NIF sin letra (8 dígitos): ").strip()
        if len(nif_numero) == 8 and nif_numero.isdigit():
            nif_numero = int(nif_numero)
            break
        else:
            print("Por favor, introduce exactamente 8 dígitos numéricos.")
    except ValueError:
        print("Entrada no válida. Introduce solo números.")

nif_letra = letra_nif(nif_numero)
print(f"El NIF completo es: {nif_numero}{nif_letra}")
