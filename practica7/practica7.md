# Práctica 07. Python. Ejercicios selección

```python
#!/usr/bin/python
#
#   1.- Escribir un programa que pida tres números enteros por teclado y determine el mayor y el
#   menor de los tres números. Ejemplo:
#       Introduzca el primer número: 20
#       Introduzca el segundo número: 34
#       Introduzca el tercer número: -18
#       Mayor número: 34
#       Menor número: -18
#
#   Victor Manuel Andreu Felipe 2025

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

# calculamos el mayor
# Consultar a Alejandro sobre si es mejor
# almacenar en variables y luego imprimir o ir imprimiendo
# y si es necesario recoger el caso de que sean los 3 iguales
# puesto que todos son el mayor y el menor

if num1 >= num2 and num1 >= num3:
#    mayor = num1
    print("Mayor número: ", num1)
elif num2 >= num1 and num2 >= num3:
#    mayor = num2
    print("Mayor número: ", num2)
else:
#    mayor = num3
    print("Mayor número: ", num3)

# calculamos el menor

if num1 <= num2 and num1 <= num3:
#    menor = num1
    print("Mayor número: ", num1)
elif num2 <= num1 and num2 <= num3:
#    menor = num2
    print("Mayor número: ", num2)
else:
#    menor = num3
    print("Menor número: ", num3)

#print("Mayor número: ", mayor)
#print("Menor número: ", menor)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   2.- Estás en un largo viaje en coche, la distancia a la próxima gasolinera es de 200 Km. Escribe un
#   programa que preguntando el tamaño del depósito, el % del combustible restante y el consumo,
#   muestre si puedes o no llegar a la gasolinera.
#       Ejemplo:
#           Tamaño del depósito (litros): 50
#           % de combustible: 50
#           Consumo (l/100 Km): 10
#           Puedes recorrer 250 Km más.
#           Espera a la próxima gasolinera.
#      Ejemplo:
#           Tamaño del depósito (litros): 50
#           % de combustible: 30
#           Consumo (l/100 Km): 10
#           Puedes recorrer 150 Km más.
#           La gasolinera está a 200 Km. ¡¡ Echa gasolina !!
#
#   ¡¡¡ ADVERTENCIA !!! No programes mientras conduces :(
#
#   Victor Manuel Andreu Felipe 2025

depo = float(input("Tamaño del depósito (litros): "))
combu = float(input("% de combustible: "))
consu = float(input("Consumo (l/100 Km): "))

km = depo * combu / 10

# control del input

if depo < 0 or combu < 0 or consu < 0:
    print("No puedes tener un depósito que te debe gasolina, ni un coche que te da combustible. Introduce valores positivos.")
else:
    print("Puedes recorrer", km, "Km más.")

    if km >= 200:
        print("Espera a la próxima gasolinera.")
    else:
        print("La gasolinera está a 200 Km. ¡¡ Echa gasolina !!")
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   3.- Escribe un programa que dada una nota numérica entre 0 y 10 con dos decimales, diga la
#   nota literal que tiene el alumno. Suponiendo:
#       Sobresaliente: nota en el intervalo [9, 10]
#       Notable: nota en el intervalo [7, 9)
#       Bien: nota en el intervalo [6, 7)
#       Suficiente: nota en el intervalo [5, 6)
#       Suspenso: nota en el intervalo [0, 5)
#       Introduzca la nota: 8.35
#       Nota: Notable
#
#   Victor Manuel Andreu Felipe 2025

nota = float(input("Introduzca la nota: "))

literal = ""

# control del input

if nota < 0 or nota > 10:
    print("La nota debe estar entre 0 y 10")
else:
    if nota < 5:
        literal = 'Insuficiente'
    elif nota >= 5 and nota < 6:
        literal = 'Suficiente'
    elif nota >= 6 and nota < 7:
        literal = 'Bien'
    elif nota >= 7 and nota < 9:
        literal = 'Notable'
    elif nota >= 9:
        literal = 'Sobresaliente'

    print("Nota: ", literal)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   4.- Escribir un programa que calcule ecuaciones de segundo grado del tipo ax²+bx+c=0. El
#   programa solicitará los coeficientes a, b y c. A continuación mostrará las soluciones.
#
#   Victor Manuel Andreu Felipe 2025

print("Solución de ecuaciones de segundo grado(con enteros)")

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

if a == 0:
    if b == 0:
        if c == 0:
            print("La ecuación: " + cstr + " = 0 tiene infinitas soluciones.")
        else:
            print("La ecuación: " + cstr + " = 0 no tiene solución real.")
    else:
        sol = -c / float(b)
        print("La ecuación: " + bstr + cstr + " = 0 es de primer grado y tiene solución x =", sol)
else:
    if disc < 0:
        print("La ecuación: " + astr + bstr + cstr + " = 0 no tiene solución real.")
    elif disc == 0:
        sol1 = -b / (2 * a)
        print("La ecuación: " + astr + bstr + cstr + " = 0 tiene una sola solución, que es x =", sol1)
    else:
        # crédito a Diego por usar las matemáticas y darme la sugerencia de ** 0.5 en vez math.square
        sol1 = (-b + disc ** 0.5) / (2 * a)
        sol2 = (-b - disc ** 0.5) / (2 * a)
        print("Las soluciones a la ecuación: " + astr + bstr + cstr + " = 0 son x1 =", sol1, "y x2 =", sol2)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   5.- Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Escribir un programa
#   que calcule el sueldo bruto mensual en euros a partir de los siguientes datos:
#       • Días trabajados.
#       • Días festivos trabajados.
#       • Turno: mañana, tarde, noche.
#   ... con las siguientes restricciones:
#       • Un día tiene 8 horas laborales.
#       • Las horas de un día normal se pagan a 12 €, las horas de un día festivo se pagan a 24€.
#       • Un trabajador en un mes, sólo puede trabajar en un turno y 8 horas al día.
#       • Los meses son de 30 días.
#       • El turno de noche se paga un 20% más que los turnos de mañana y tarde.
#   Ejemplo:
#       Días trabajados: 22
#       Días festivos trabajados: 5
#       Turno (M-mañana, T-tarde, N-noche): M
#       Sueldo: 3072 euros
#
#   Victor Manuel Andreu Felipe 2025

dlab = int(input("Días trabajados: "))
dfest = int(input("Días festivos trabajados: "))
turno = str(input("Turno (M-mañana, T-tarde, N-noche): "))

# primero controlamos las restricciones de horas y días

if dlab < 0 or dfest < 0:
    print("No se pueden trabajar horas negativas")
elif dlab == 0 and dfest == 0:
    print("Esta persona no ha trabajado con nosotros")
elif dlab + dfest > 30:
    print("No hay tantos días en un mes")
else:
    # y luego controlamos el turno
    if turno == 'N':
        sueldo = dlab * 8 * 12 * 1.2 + dfest * 8 * 24 * 1.2
        print("Sueldo:", sueldo, "euros")
    elif turno == 'M' or turno == 'T':
        sueldo = dlab * 8 * 12 + dfest * 8 * 24
        print("Sueldo:", sueldo, "euros")
    else:
        print("Ese turno no existe")
```

<div style="page-break-after: always;"></div>

```python
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
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   7.- Escribir un programa que dada una fecha en el formato DIA/MES/AÑO, diga si la fecha es
#   correcta o incorrecta. Si la fecha es correcta el programa debe escribirla con el formato DIA de
#   MES de AÑO.
#   Ejemplo:
#       Introduzca una fecha: 24/12/2004
#       La fecha es 24 de diciembre de 2004
#   Ejemplo:
#       Introduzca una fecha: 31/02/2003
#       La fecha es incorrecta
#   Nota: hay que controlar los años bisiestos, según Wikipedia:
#   "Un año es bisiesto si es divisible entre 4, a menos que sea divisible entre 100. Sin
#   embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta
#   bisiesto. Obviamente, esto elimina los años finiseculares (últimos de cada siglo, que ha de
#   terminar en 00) divisibles solo entre 4 y entre 100.”
#   Dicho de otra forma, un año es bisiesto si:
#   “(si es divisible por 4 Y no es divisible por 100) O es divisible por 400.
#
#   Victor Manuel Andreu Felipe 2025
#   
#   Como no se pueden usar listas, no conozco la forma de pedir la fecha en DD/MM/YY y luego dividirla

dia = int(input("Introduzca el día del mes: "))
mes = int(input("Introduzca el mes en número: "))
ano = int(input("Introduzca el año: "))

# comprobamos que los meses y los días esten correctos

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 0 or dia > 31:
        corr = "incorrecta"
    else:
        corr = "correcta"
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 0 or dia > 30:
        corr = "incorrecta"
    else:
        corr = "correcta"
# comprobamos los años bisiestos (tengo una duda, 
# ¿un año negativo(antes de cristo) puede ser bisiesto?)
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 0 or dia > 29:
            corr = "incorrecta"
        else:
            corr = "correcta"
    else: 
        if dia <= 0 or dia > 28:
            corr = "incorrecta"
        else:
            corr = "correcta"
else:   # aqui comprobamos que los meses estén entre 1 y 12
    corr = "incorrecta"

# asignación de nombre a los meses numéricos

if mes == 1:
    mes = "Enero"
elif mes == 2:
    mes = "Febrero"
elif mes == 3:
    mes = "Marzo"
elif mes == 4:
    mes = "Abril"
elif mes == 5:
    mes = "Mayo"
elif mes == 6:
    mes = "Junio"
elif mes == 7:
    mes = "Julio"
elif mes == 8:
    mes = "Agosto"
elif mes == 9:
    mes = "Septiembre"
elif mes == 10:
    mes = "Octubre"
elif mes == 11:
    mes = "Noviembre"
elif mes == 12:
    mes = "Diciembre"

if corr == "correcta":
    print("La fecha es " + str(dia) + " de " + str(mes) + " de " + str(ano))
else:
    print("La fecha es", corr)
```

<div style="page-break-after: always;"></div>

```python
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
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    9.- Escribir un programa que pida cuatro números enteros por teclado y determine el mayor y el
#    menor de los cuatro números. Ejemplo:
#       Introduzca 4 números enteros: 20 34 10 -18
#       Mayor número: 34
#       Menor número: -18
#
#   Victor Manuel Andreu Felipe 2025
#
#   Como no se pueden usar listas, no conozco la manera de pedir los cuatro números de una vez

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))
num4 = int(input("Introduzca el cuarto número: "))

# calculamos el mayor
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print("Mayor número:", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("Mayor número:", num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("Mayor número:", num3)
else:
    print("Mayor número:", num4)

# calculamos el menor
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    print("Menor número:", num1)
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    print("Menor número:", num2)
elif num3 <= num1 and num3 <= num2 and num3 <= num4:
    print("Menor número:", num3)
else:
    print("Menor número:", num4)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    10.- Escribe un programa que dada una hora en el formato hh:mm:ss muestre la hora siguiente.
#    Ejemplo:
#       Hora: 23:58:59
#       23:59:00
#    Ejemplo:
#       Hora: 23:63:59
#       La hora es incorrecta
#
#   Victor Manuel Andreu Felipe 2025
#
# Como no se pueden usar listas, no se recoger la hora en hh:mm:ss

hour = int(input("Hora: "))
min = int(input("Minutos: "))
sec = int(input("Segundos: "))
if (hour < 0 or hour > 23 or
    min < 0 or min > 59 or
    sec < 0 or sec > 59):
    print("La hora es incorrecta")
else:   # incrementamos la hora en 1 segundo
    sec += 1
    if sec == 60:   # comprobamos los valores tope y reseteamos en caso necesario
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if hour == 24:
        hour = 0
 
    hourlit = str(hour)
    # si los valores son menor que 10, agregamos un 0 la izquierda
    if min < 10:
        minlit = "0" + str(min)
    else:
        minlit = str(min)
    if sec < 10:
        seclit = "0" + str(sec)
    else:
        seclit = str(sec)
    print(hourlit + ":" + minlit + ":" + seclit)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    10.- Escribe un programa que dada una hora en el formato hh:mm:ss muestre la hora siguiente.
#    Ejemplo:
#       Hora: 23:58:59
#       23:59:00
#    Ejemplo:
#       Hora: 23:63:59
#       La hora es incorrecta
#
#   Victor Manuel Andreu Felipe 2025
#

cadena = str(input("Hora(HH/MM/SS): "))

partes = cadena.split(":")

# comprobación de formato

if len(partes) != 3:
    print("Hora incorrecta, por favor, use el formato HH:MM:SS")
else:

    hour = int(partes[0])
    min = int(partes[1])
    sec = int(partes[2])

    if (hour < 0 or hour > 23 or
        min < 0 or min > 59 or
        sec < 0 or sec > 59):
        print("La hora es incorrecta")
    else:   # incrementamos la hora en 1 segundo
        sec += 1

        if sec == 60:   # comprobamos los valores tope y reseteamos en caso necesario
            sec = 0
            min += 1

        if min == 60:
            min = 0
            hour += 1

        if hour == 24:
            hour = 0
    
        hourlit = str(hour)

        # si los valores son menor que 10, agregamos un 0 la izquierda
        if min < 10:
            minlit = "0" + str(min)
        else:
            minlit = str(min)

        if sec < 10:
            seclit = "0" + str(sec)
        else:
            seclit = str(sec)

        print(hourlit + ":" + minlit + ":" + seclit)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    11.- Programa que lee la nota de 5 alumnos y dice cuántos están aprobados y cuál es la nota
#    media. Para este ejercicio no se pueden utilizar bucles.
#        Nota del alumno 01: 5.60
#        Nota del alumno 02: 4.20
#        Nota del alumno 03: 8.35
#        Nota del alumno 04: 7.23
#        Nota del alumno 05: 5.01
#        Aprobados: 4
#        Suspensos: 1
#        Nota media: 6.08
#
#   Victor Manuel Andreu Felipe 2025
#   

apro = 0    # iniciamos los contadores
susp = 0

nota1 = int(input("Nota del alumno 01: "))
nota2 = int(input("Nota del alumno 02: "))
nota3 = int(input("Nota del alumno 03: "))
nota4 = int(input("Nota del alumno 04: "))
nota5 = int(input("Nota del alumno 05: "))

# control de rangos

if (nota1 < 0 or nota1 > 10 or
    nota2 < 0 or nota2 > 10 or
    nota3 < 0 or nota3 > 10 or
    nota4 < 0 or nota4 > 10 or
    nota5 < 0 or nota5 > 10):
    print("Deben ser notas entre 0 y 10")
else:
    # incrementamos aprobados o suspensos
    if nota1 < 5:
        susp += 1
    else:
        apro += 1

    if nota2 < 5:
        susp += 1
    else:
        apro += 1

    if nota3 < 5:
        susp += 1
    else:
        apro += 1

    if nota4 < 5:
        susp += 1
    else:
        apro += 1

    if nota5 < 5:
        susp += 1
    else:
        apro += 1

    print("Aprobados: ", apro)
    print("Suspensos: ", susp)
    print("Nota media: ", (nota1 + nota2 + nota3 + nota4 + nota5) / 5)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    11.- Programa que lee la nota de 5 alumnos y dice cuántos están aprobados y cuál es la nota
#    media. Para este ejercicio no se pueden utilizar bucles.
#        Nota del alumno 01: 5.60
#        Nota del alumno 02: 4.20
#        Nota del alumno 03: 8.35
#        Nota del alumno 04: 7.23
#        Nota del alumno 05: 5.01
#        Aprobados: 4
#        Suspensos: 1
#        Nota media: 6.08
#
#   Victor Manuel Andreu Felipe 2025
#   

apro = 0    # iniciamos los contadores
susp = 0

nota1 = float(input("Nota del alumno 01: "))
nota2 = float(input("Nota del alumno 02: "))
nota3 = float(input("Nota del alumno 03: "))
nota4 = float(input("Nota del alumno 04: "))
nota5 = float(input("Nota del alumno 05: "))

# control de rangos

if (nota1 < 0 or nota1 > 10 or
    nota2 < 0 or nota2 > 10 or
    nota3 < 0 or nota3 > 10 or
    nota4 < 0 or nota4 > 10 or
    nota5 < 0 or nota5 > 10):
    print("Deben ser notas entre 0 y 10")
else:
    # incrementamos aprobados o suspensos
    if nota1 < 5:
        susp += 1
    else:
        apro += 1

    if nota2 < 5:
        susp += 1
    else:
        apro += 1

    if nota3 < 5:
        susp += 1
    else:
        apro += 1

    if nota4 < 5:
        susp += 1
    else:
        apro += 1

    if nota5 < 5:
        susp += 1
    else:
        apro += 1

    print("Aprobados: ", apro)
    print("Suspensos: ", susp)
    print("Nota media: ", (nota1 + nota2 + nota3 + nota4 + nota5) / 5)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   12.- Programa que lee un número y muestra la tabla de num1plicar de dicho número. Para este
#   ejercicio no se pueden utilizar bucles.
#       Número: 8
#       8 x 0 = 0
#       8 x 1 = 8
#       8 x 2 = 16
#       8 x 3 = 24
#       8 x 4 = 32
#       8 x 5 = 40
#       8 x 6 = 48
#       8 x 7 = 56
#       8 x 8 = 64
#       8 x 9 = 72
#       8 x 10 = 80
#
#   Victor Manuel Andreu Felipe 2025

num1 = int(input("Número: "))
num2 = 0

print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
num2 += 1
print(num1, "x",num2, "=", num1 * num2)
```