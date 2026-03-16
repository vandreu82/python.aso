#!/usr/bin/python
#
#   7.- Escribe un programa que lea una cadena de texto, acto seguido debe comprobar que se trata
#   de un número de NIF correcto, 8 dígitos y una letra. El programa debe contar con la función
#   es_nif que devuelva si el NIF es o no correcto
#   La función debe calcular la letra según el parámetro pasado, calcular la letra
#   correspondiente a un NIF es bastante sencillo, hay que realizar la división entera del número del
#   NIF entre 23, se toma el resto y se asigna una letra según la siguiente tabla:
#   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
#   T R W A G M Y F P D  X  B  N  J  Z  S  Q  V  H  L  C  K  E
#
#   Victor Manuel Andreu Felipe 2025

import re

# comprobamos si es correcto el nif(permitimos un guión)
def es_nif(nif):
    letras_nif = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # quitamos el posible guión
    nif = nif.replace("-", "").strip()
    
    # lo comprobamos con un regex
    if not re.fullmatch(r"\d{8}[A-Za-z]", nif):
        return False
    
    numero = int(nif[:-1])  # sacamos los numeros
    letra_correcta = letras_nif[numero % 23]  # calculamos la letra
    letra_usuario = nif[-1].upper()  # la subimos a mayúsculas
    
    return letra_correcta == letra_usuario # compadamos ambas letras y devolvemos true o false

# con strip eliminamos los espacios
nif = input("Introduce un NIF (8 dígitos + letra, con o sin guion): ").strip()

if es_nif(nif):
    print("El NIF es correcto")
else:
    print("El NIF es incorrecto")

