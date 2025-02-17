# Práctica 08. Python. Ejercicios bucles

```python
#!/usr/bin/python
#
#   1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número. Hacer el
#   ejercicio de dos formas, con bucle while y con bucle for.
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

num = int(input("Número: "))

for i in range(0, 11):
    print(num, "x",i, "=", num * i)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número. Hacer el
#   ejercicio de dos formas, con bucle while y con bucle for.
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

num = int(input("Número: "))
i = 0

while i < 11:
    print(num, "x",i, "=", num * i)
    i += 1
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   2.- Escribir un programa que imprima las 10 tablas de multiplicar.
#
#   Victor Manuel Andreu Felipe 2025

for i in range(0, 11):
    print("")   # separador
    for j in range (0, 11):
        print(i, "x",j, "=", i * j)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   3.- Programa que lee notas de los alumnos y dice cuántos están aprobados y cuál es la nota
#   media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.
#       Introduzca las notas, ENTER para terminar:
#       Nota del alumno 1: 5.60
#       Nota del alumno 2: 4.20
#       Nota del alumno 3: 8.35
#       Nota del alumno 4: 7.23
#       Nota del alumno 5: 5.01
#       Nota del alumno 6: (pulsamos ENTER)
#       Número de alumnos: 5
#       Aprobados: 4
#       Suspensos: 1
#       Nota media: 6.08
#
#   Victor Manuel Andreu Felipe 2025

print("Introduzca las notas, ENTER para terminar: ")

alu = 0
apro = 0
susp = 0
notasum = 0

while True:
    notastr = input("Nota del alumno " + str(alu + 1) + ": ")
    
    # el bucle se ejecutará siempre excepto cuando le metamos una cadena vacía
    if notastr == "":       
        break
    
    # convertimos la nota a float y comprobamos que sea correcta, si no, volvemos 
    # a iterar sin hacer nada
    nota = float(notastr)
    if nota < 0 or nota > 10:
        print("La nota debe estar comprendida entre 0 y 10")
        continue

    # acumulamos el número de alumnos y la suma de las notas
    # para calcular la media mas tarde
    alu += 1
    notasum += nota

    # incrementamos aprobados y suspensos
    if nota >= 5:
        apro += 1
    else:
        susp += 1

# comprobamos que haya notas

if alu > 0:
    print("Número de alumnos: ", alu)
    print("Aprobados: ", apro)
    print("Suspensos: ", susp)
    print("Nota media: ", notasum / alu)
else:
    print("No has introducido notas")

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   4.- Escribir un programa que solicite un número positivo, acto seguido debe calcular la suma de
#   todos los números pares comprendidos entre 0 y el numero solicitado. Ejemplo:
#       Introduzca un número: 341
#       La suma es: 29070
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    suma = 0
    i = 0
    while i <= num:
        suma += i
        i += 2  # acumulación para sumar solo los pares

    print("La suma es:", suma)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   5.- Escribe un programa que dado un número, muestre todos los múltiplos de 11 desde el cero
#   hasta el número.
#       Introduzca un número: 125
#       Los múltiplos son: 0 , 11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 , 99 ,
#       110 , 121
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    i = 0
    multi = ""  # cadena para guardar los múltiplos

    while i <= num:
        if multi == "":     # si está vacia(iteración inicial), no 
            multi = str(i)  # imprimimos coma
        else:
            multi = multi + " , " + str(i)
        i += 11             # iteramos de 11 en 11
    
    print("Los múltiplos son:", multi)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   6.- Escribir un programa que muestre la tabla ASCII. Extracto:
#       Tabla ASCII (caracteres de 32 a 126):
#       …
#       60 => <
#       61 => =
#       62 => >
#       63 => ?
#       64 => @
#       65 => A
#       66 => B
#       ...
#
#   Victor Manuel Andreu Felipe 2025

print("Tabla ASCII (caracteres de 32 a 126):")

for i in range(32, 127):
    print(i,"=>",chr(i))
```

<div style="page-break-after: always;"></div>


```python
#!/usr/bin/python
#
#   7.- Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
#   se introduzca el cero. A continuación debe mostrar el mayor número. Ejemplo:
#       Introduzca un número (cero para terminar): 1230
#       Introduzca un número (cero para terminar): 0.023
#       Introduzca un número (cero para terminar): 12.23
#       Introduzca un número (cero para terminar): 3.1415
#       Introduzca un número (cero para terminar): 280
#       Introduzca un número (cero para terminar): 4234.6
#       Introduzca un número (cero para terminar): 0
#       Mayor: 4234.6
#
#   Victor Manuel Andreu Felipe 2025

num = float(input("Introduzca un número (cero para terminar): "))

if num == 0:
    print("Fin del programa")
else:
    mayor = num 

    while True:
        num = float(input("Introduzca un número (cero para terminar):"))

        if num == 0:
            break

        if num > mayor:
            mayor = num

    print("Mayor:", mayor)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   8.- Escribir un programa que “dibuje” un mes del calendario. El programa recibirá como entrada el
#   número de días del mes y el día de la semana del primer día del mes. Ejemplo:
#       Número de días del mes: 31
#       Día 1 es (0 lunes, 6 domingo): 4
#       L  M  X  J  V  S  D
#                   1  2  3
#       4  5  6  7  8  9 10
#      11 12 13 14 15 16 17
#      18 19 20 21 22 23 24
#      25 26 27 28 29 30 31
#
#   Victor Manuel Andreu Felipe 2025

# control de errores
num = 0
while num < 1 or num > 31:
    num = int(input("Número de días del mes: "))
    if num < 1 or num > 31:
        print("Error: Un mes tiene entre 1 y 31 días.")

diasem = -1
while diasem < 0 or diasem > 6:
    diasem = int(input("Día 1 es (0 lunes, 6 domingo): "))
    if diasem < 0 or diasem > 6:
        print("Error: Debe ser un número entre 0 y 6.")

# cabecera
print(" L  M  X  J  V  S  D")

fila = ""   # Variable que será la salida por pantalla
            # donde vamos a ir concatenando cosas

for i in range(diasem): # bucle para agregar 3 espacios por cada                        
    fila += "   "       # por cada día de la semana en el que empecemos

cont = diasem           # contador para movernos por la fila

for diasem in range(1, num + 1):
    if diasem < 10:     # si el día de la semana solo tiene una cifra
                        # se imprime un espacio a la izquierda
        fila += " " + str(diasem) + " "
    else:
        fila+= str(diasem) + " "

    cont += 1

    if cont == 7:       # con esto reiniciamos la fila cada domingo
        print(fila)
        cont = 0
        fila = ""

print(fila)
 
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   9.- Escribir un programa para calcular superficies. Constará de un menú que solicitará la figura a
#   la que se va a calcular la superficie, pedirá los datos (lado, base y altura, radio ...) según la figura
#   de la que se trate y visualizará el resultado. El programa deberá calcular superficies de las
#   siguientes figuras: cuadrados, triángulos y círculos. Ejemplo:
#       Cálculo de superficies:
#       1.- Cuadrados
#       2.- Triángulos
#       3.- Círculos
#       4.- Salir
#       Elija opción (1-4): 1
#       Lado: 8
#       La superficie es de 64 cm²
#       (mostramos de nuevo el menú...)
#
#   Victor Manuel Andreu Felipe 2025

while True:         # el bucle se ejecuta siempre, solo salimos con '4'
    print("Cálculo de superficies:")
    print("1.- Cuadrados")
    print("2.- Triángulos")
    print("3.- Círculos")
    print("4.- Salir")
    opcion = input("Introduzca un número: ")
    print()     # linea para presentación

    if (opcion == '4'):
        print("Adios")  
        exit(0)

    if opcion == '1':
        lado = float(input("Lado: "))
        print("La superficie es de: ", lado ** 2, "cm²")

    elif opcion == '2':
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("La superficie es de: ", base * altura / 2, "cm²")

    elif opcion == '3':
        radio = float(input("Radio: "))
        print("La superficie es de: ", 3.1416 * radio ** 2, "cm²")
    
    # control de errores
    else: print("Opción inválida. Introduzca un número entre 1 y 4.")

    print() # linea para presentacion
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#    10.- Escribir un programa que tome 100 números aleatorios entre 0 y 99. A continuación debe
#    mostrar cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y
#    [80-99]. Ejemplo:
#       [ 0-19]: 12
#       [20-39]: 34
#       [40-59]: 20
#       [60-79]: 15
#       [80-99]: 19
#       Total: 100
#
#   Victor Manuel Andreu Felipe 2025

import random

ran1 = 0
ran2 = 0
ran3 = 0
ran4 = 0
ran5 = 0

for i in range(1, 101, 1):
    num = random.randint(1, 99)
    if num >= 0 and num <= 19:
        ran1 += 1
    elif num >= 20 and num <39:
        ran2 += 1
    elif num >= 40 and num <59:
        ran3 += 1
    elif num >= 60 and num <79:
        ran4 += 1
    else:
        ran5 += 1

print("[ 0-19]: ", ran1)
print("[20-39]: ", ran2)
print("[40-59]: ", ran3)
print("[60-79]: ", ran4)
print("[80-99]: ", ran5)
print("Total: ", i)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   11.- Escribir un programa que calcule el factorial de un número dado. Ejemplo:
#       Introduce un número: 7
#       7! = 5040
#
#   Victor Manuel Andreu Felipe 2025
#   código reciclado absolutamente del sumatorio de números pares

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num < 0:
    print("El número debe ser positivo")
else:
    facto = 1
    i = 1
    while i <= num:
        facto =  facto * i
        i += 1

    print(str(num) + "! =", facto)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   12.- Escribir un programa que solicite un número n y a continuación muestre si el número es o no
#   primo. Ejemplos:
#       Introduzca un número: 100
#       El número no es primo
#       Introduzca un número: 101
#       El número es primo
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num <= 0:
    print("El número debe ser positivo")
elif num == 1:
    print("El número no es primo")  # excepcion del 1 que no es primo
else:
    i = 2           # empezamos en el 2 porque el 1 no es primo
    corr = ""       
    while i < num:          # bucle que recorre todos los números anteriores
        if num % i == 0:    # dividiéndolo entre ellos buscando divisores
            corr = "no "
            break
        i += 1

    print("El número " + corr + "es primo")
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   13.- Escribir un programa que solicite un número n y a continuación imprima todos los números
#   primos comprendidos en el intervalo [2-n]. Ejemplo:
#       Introduzca un número: 100
#       Números primos [2-100]: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97
#
#   Victor Manuel Andreu Felipe 2025
#
#############################   terminar luego

num = int(input("Introduzca un número: "))

# comprobamos que no sea un número negativo
if num <= 0:
    print("El número debe ser positivo")
elif num == 1:
    print("El número 1 no tiene intervalo de primos")  # excepcion del 1 que no es primo
else:
    i = 2           # empezamos en el 2 porque el 1 no es primo
    inter = ""       
    while i <= num:          # bucle que recorre todos los números anteriores
        if num % i == 0:    # dividiéndolo entre ellos buscando divisores
            es_primo = False
        else:
            es_primo = True
        i += 1
        while es_primo == True:
            inter += inter
            
    print("Números primos [2-" + str(num) + "]: " + inter)
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   14.- Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de
#   la figura.
#       Nivel: 4
#           XX 
#          XXXX
#         XXXXXX
#        XXXXXXXX
#
#       Nivel: 3
#           X
#          XXX
#         XXXXX
#
#       Nivel: 2
#           XX
#          XXXX
#
#   Victor Manuel Andreu Felipe 2025

num = int(input("Nivel: "))

# comprobacion de rango
if num < 2 or num > 40:
    print("El número debe estar entre 2 y 40")
else:
    i = 1
    while i <= num:
        espa = num - i  # ajustamos el espaciado inicial
        # imprimimos la línea con espacios y el doble de X por número de línea
        # el espaciado de la derecha no es necesario pues saltamos de línea
        print(" " * espa + "X" * (2 * i))
        i += 1  # pasamos a la siguiente línea
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   15.- Escribir un programa que dándole un número (entre 2 y 40) imprima un rombo como el de la
#   figura. Ejemplo:
#       num: 4
#       XXXXXXXX
#       XXX  XXX
#       XX    XX
#       X      X
#       X      X
#       XX    XX
#       XXX  XXX
#       XXXXXXXX
#
#   Victor Manuel Andreu Felipe 2025
# Este programa es parecido al anterior pero se imprime al revés y en fases.
# Y aquí si hay que tener en cuenta el lado derecho.

num = int(input("Nivel: "))

# comprobacion de rango
if num < 2 or num > 40:
    print("El número debe estar entre 2 y 40")
else:
    i = 0  
    while i < num:     # imprimimos la primera mitad
        print("X" * (num - i) + " " * (2 * i) + "X" * (num - i))
        i += 1

    i = num - 1        # y la segunda mitad la imprimimos al revés
    while i >= 0:
        print("X" * (num - i) + " " * (2 * i) + "X" * (num - i))
        i -= 1

```

<div style="page-break-after: always;"></div>

```python
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

```

<div style="page-break-after: always;"></div>

