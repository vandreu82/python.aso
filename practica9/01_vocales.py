#!/usr/bin/python
#
#   1.- Escribe un programa que cuente el número de vocales de una frase.
#          Introduzca una frase: Hola a todos
#          Vocales: a(2), e(0), i(0), o(3), u(0)
#
#   Victor Manuel Andreu Felipe 2025

def contar_vocales(frase):
    a = e = i = o = u = 0  # contadores para cada vocal

    for letra in frase.lower():  # bajamos a minusculas para pasar por el if
        if letra == 'a':
            a += 1
        elif letra == 'e':
            e += 1
        elif letra == 'i':
            i += 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1

    print(f"Vocales: a({a}), e({e}), i({i}), o({o}), u({u})")

# Solicitar la frase al usuario
frase = input("Introduzca una frase: ")

contar_vocales(frase)