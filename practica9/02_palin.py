#!/usr/bin/python
#
#   2.- Un palíndromo es una frase o palabra que se lee igual en un sentido u en otro. Escribe una
#   función que determine si una cadena es o no un palíndromo. Ej.: “Dabale arroz a la zorra el abad”
#   es un palíndromo; “Somos o no somos”, “Luz azul”, “La Ruta Natural”, también lo son.
#   Escribir una función que determine si una cadena es o no un palíndromo.
#       Introduzca una frase: Hola a todos
#       La frase no es un palíndromo
#       Introduzca una frase: Luz azul
#       La frase es un palíndromo
#
#   Victor Manuel Andreu Felipe 2025

def es_palindromo(frase):
    # con join eliminamos espacios, con lower bajamos a minúsculas y con isalnum comprobamos que sean alfanuméricos
    frasetrim = ''.join(letra.lower() for letra in frase if letra.isalnum())
    
    # recorremos la frase desde el final hasta el principio y la comparamos
    if frasetrim == frasetrim[::-1]:
        print("La frase es un palíndromo")
    else:
        print("La frase no es un palíndromo")

frase = input("Introduzca una frase: ")

es_palindromo(frase)