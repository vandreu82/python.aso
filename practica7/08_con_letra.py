#!/usr/bin/python
#
#   8.- Escribir un programa que pida un número comprendido entre 0 y 100. A continuación debe
#   escribir el número “con letra”.
#       Introduzca un número entre 0 y 100: 38
#       El número introducido es el treinta y ocho.
#
#   Victor Manuel Andreu Felipe 2025
#   
#   Este ejercicio es horrible y sabes perfectamente que vamos a usar IA para hacerlo :)

num = int(input("Introduzca un número entre 0 y 100: "))

if num < 0 or num > 100:    # comprobación de rango
    print("Debe ser un número entre 0 y 100")
# las treinta y ocho excepciones
elif num == 0:              
    print("El número introducido es el cero.")
elif num == 1:
    print("El número introducido es el uno.")
elif num == 2:
    print("El número introducido es el dos.")
elif num == 3:
    print("El número introducido es el tres.")
elif num == 4:
    print("El número introducido es el cuatro.")
elif num == 5:
    print("El número introducido es el cinco.")
elif num == 6:
    print("El número introducido es el seis.")
elif num == 7:
    print("El número introducido es el siete.")
elif num == 8:
    print("El número introducido es el ocho.")
elif num == 9:
    print("El número introducido es el nueve.")
elif num == 10:
    print("El número introducido es el diez.")
elif num == 11:
    print("El número introducido es el once.")
elif num == 12:
    print("El número introducido es el doce.")
elif num == 13:
    print("El número introducido es el trece.")
elif num == 14:
    print("El número introducido es el catorce.")
elif num == 15:
    print("El número introducido es el quince.")
elif num == 16:
    print("El número introducido es el dieciséis.")
elif num == 17:
    print("El número introducido es el diecisiete.")
elif num == 18:
    print("El número introducido es el dieciocho.")
elif num == 19:
    print("El número introducido es el diecinueve.")
elif num == 20:
    print("El número introducido es el veinte.")
elif num == 21:
    print("El número introducido es el veintiuno.")
elif num == 22:
    print("El número introducido es el veintidós.")
elif num == 23:
    print("El número introducido es el veintitrés.")
elif num == 24:
    print("El número introducido es el veinticuatro.")
elif num == 25:
    print("El número introducido es el veinticinco.")
elif num == 26:
    print("El número introducido es el veintiséis.")
elif num == 27:
    print("El número introducido es el veintisiete.")
elif num == 28:
    print("El número introducido es el veintiocho.")
elif num == 29:
    print("El número introducido es el veintinueve.")
elif num == 30:
    print("El número introducido es el treinta.")
elif num == 40:
    print("El número introducido es el cuarenta.")
elif num == 50:
    print("El número introducido es el cincuenta.")
elif num == 60:
    print("El número introducido es el sesenta.")
elif num == 70:
    print("El número introducido es el setenta.")
elif num == 80:
    print("El número introducido es el ochenta.")
elif num == 90:
    print("El número introducido es el noventa.")
elif num == 100:
    print("El número introducido es el cien.")
else:
# dividimos los dígitos y declaramos las cadenas de las cifras en letra
    dec = int(num / 10)
    uni = int(num % 10)
    decl = str("")
    unil = str("")
# construimos la cadena en base a las decenas y las unidades
    if dec == 3:
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
    print("El número introducido es el", decl, "y", unil)