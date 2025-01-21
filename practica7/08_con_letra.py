#!/usr/bin/python
#
#   8.- Escribir un programa que pida un número comprendido entre 0 y 100. A continuación debe
#   escribir el número “con letra”.
#       Introduzca un número entre 0 y 100: 38
#       El número introducido es el treinta y ocho.
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número entre 0 y 100: "))

texto = "El número introducido es el"

if num < 0 or num > 100:    # comprobación de rango
    print("Debe ser un número entre 0 y 100")
# las excepciones
elif num == 0:              
    print(texto, "cero.")
elif num == 10:
    print(texto, "diez.")
elif num == 11:
    print(texto, "once.")
elif num == 12:
    print(texto, "doce.")
elif num == 13:
    print(texto, "trece.")
elif num == 14:
    print(texto, "catorce.")
elif num == 15:
    print(texto, "quince.")
elif num == 20:
    print(texto, "veinte")
elif num == 100:
    print(texto, "cien.")
else:
# dividimos los dígitos y declaramos las cadenas de las cifras en letra
    dec = int(num / 10)
    uni = int(num % 10)
    decl = str("")
    unil = str("")
# construimos la cadena en base a las decenas y las unidades
    if dec == 2:
        decl = "veinti"
    elif dec == 3:
        decl = "treinta"
    elif dec == 4:
        decl = "cuarenta"
    elif dec == 5:
        decl = "cincuenta"
    elif dec == 6:
        decl = "sesenta"
    elif dec == 7:
        decl = "setenta"
    elif dec == 8:
        decl = "ochenta"
    elif dec == 9:
        decl = "noventa"

    if uni == 1:
        unil += "uno."
    elif uni == 2:
        unil += "dos."
    elif uni == 3:
        unil += "tres."
    elif uni == 4:
        unil += "cuatro."
    elif uni == 5:
        unil += "cinco."
    elif uni == 6:
        unil += "seis."
    elif uni == 7:
        unil += "siete."
    elif uni == 8:
        unil += "ocho."
    elif uni == 9:
        unil += "nueve."
    # imprimimos dependiendo de los valores
    if num < 10:
        print(texto, unil)
    elif num >= 16 and num < 20:
        decl = "dieci"
        print(texto, decl + unil, sep=' ')
    elif num >= 21 and num < 30:
        print(texto, decl + unil, sep=' ')
    elif num > 30 and num < 100 and num % 10 != 0:
        print(texto, decl, "y", unil)
    else:
        print(texto, decl)