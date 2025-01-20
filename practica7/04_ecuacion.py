#!/usr/bin/python
#
#   4.- Escribir un programa que calcule ecuaciones de segundo grado del tipo ax²+bx+c=0. El
#   programa solicitará los coeficientes a, b y c. A continuación mostrará las soluciones.
#
#   Victor Manuel Andreu Felipe 2025

a = int(input('Dame el valor de a: '))
b = int(input('Dame el valor de b: '))
c = int(input('Dame el valor de c: '))

# Vamos a intentar pintar bien la ecuación que me gusta que quede bonita

astr = ""
bstr = ""
cstr = ""

if a != 0:  # si a es 0 no pintará nada. si es 1 o -1 no pintara el digito
    if a == 1:
        astr = "x² "
    elif a == -1:
        astr = "-x² "
    else:
        astr = str(a) + "x² "

if b != 0:  # si b es 0 no pintará nada. si es 1 o -1 no pintara el digito
    if a != 0:
        if b == 1:
            bstr = "+ x "
        elif b == -1:
            bstr = "- x "
        else:   # si b es positivo pintará un + con espacio, si es negativo
                # le cambiamos el signo a falta de conocer alguna función
                # que de un valor ABSoluto ;) pintamos un - con espacio
            if b > 0:
                bstr = "+ " + str(b)+"x "
            else:
                bstr = "- " + str(-b)+"x "
    else:
        bstr = str(b) + "x "  # si a es 0, trataremos b como si fuera a


if c != 0:
    if a != 0 or b != 0:
        if c > 0:
            cstr = "+ " + str(c)
        else:
            cstr = "- " + str(-c) 
    else:
        cstr = str(c)

disc = b * b - 4 * a * c

if disc < 0:
    print("La ecuación: " + astr + bstr + cstr + " = 0 no tiene solución real.")
elif disc == 0:
    sol1 = -b / (2 * a)
    print("La ecuación: " + astr + bstr + cstr + " = 0 tiene una sola solución, que es x =", int(sol1))
else:
    sol1 = (-b + disc ** 0.5) / (2 * a)
    sol2 = (-b - disc ** 0.5) / (2 * a)
    print("Las soluciones a la ecuación: " + astr + bstr + cstr + " = 0 son x1 =", int(sol1), "y x2 =", int(sol2))
