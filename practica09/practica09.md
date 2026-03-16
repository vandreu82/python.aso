# Práctica 09. Python. Funciones

```python
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
    
frase = input("Introduzca una frase: ")

contar_vocales(frase)
```

<div style="page-break-after: always;"></div>

```python
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
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   3.- Escribe un programa que vaya leyendo notas de alumnos, el programa dejará de pedir notas
#   cuando se pulse la tecla ENTER, al terminar el programa mostrará las notas de los alumnos y un
#   resumen de aprobados y suspensos incluyendo la nota media:
#       Introduzca las notas, ENTER para terminar:
#           Nota del alumno 1: 5.60
#           Nota del alumno 2: 4.20
#           Nota del alumno 3: (pulsamos ENTER)
#       Se han introducido las siguientes notas:
#           Alumno 01: 5.60
#           Alumno 02: 4.20
#       Resumen:
#           Número de alumnos: 2
#           Aprobados: 1
#           Suspensos: 1
#           Nota media: 4.9
#
#   Victor Manuel Andreu Felipe 2025

def leer_notas():
    notas = []
    contador = 1

    print("Introduzca las notas, ENTER para terminar:")
    while True:
        entrada = input(f"Nota del alumno {contador}: ")
        
        if entrada == "":  # salida
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:  # comprobación de nota
                notas.append(nota) # acumulación de notas
                contador += 1
            else:
                print("Por favor, introduce una nota entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Introduce un número o pulsa ENTER para terminar.")

    return notas

def mostrar_resumen(notas):
    print("\nSe han introducido las siguientes notas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Alumno {i:02d}: {nota:.2f}") # formateo

    aprobados = sum(1 for nota in notas if nota >= 5)
    suspensos = len(notas) - aprobados
    nota_media = sum(notas) / len(notas) if notas else 0

    print("\nResumen:")
    print(f"Número de alumnos: {len(notas)}")
    print(f"Aprobados: {aprobados}")
    print(f"Suspensos: {suspensos}")
    print(f"Nota media: {nota_media:.2f}")
    
notas = leer_notas()
mostrar_resumen(notas)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   4.- Escribe un programa que pida nombres. Tras pedirlos debe mostrarlos ordenados.
#   Ejemplo:
#       Introduce nombres. ENTER para terminar
#       luis
#       javier
#       alejandro
#       francisco
#       --pulsamos ENTER--
#       Los nombres son:
#       alejandro
#       francisco
#       javier
#       luis
#
#   Victor Manuel Andreu Felipe 2025

def leer_nombres():
    nombres = []

    print("Introduce nombres. ENTER para terminar")
    while True:
        nombre = input().strip()  # quitamos espacios iniciales y finales

        if nombre == "":  # salida
            break
        
        nombres.append(nombre)  # acumula nombres

    return nombres

def mostrar_nombres_ordenados(nombres):
    print("\nLos nombres son:")
    for nombre in sorted(nombres):  # ordenamos
        print(nombre)

nombres = leer_nombres()
mostrar_nombres_ordenados(nombres)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   5.- Escribir un programa que pida un número entre 0 y 400, a continuación debe calcular todos
#   los factoriales entre el cero y el número solicitado. El programa debe tener una función factorial
#   que realice el cálculo. Ejemplo:
#       Introduce un número: 5
#       0! = 1
#       1! = 1
#       2! = 2
#       3! = 6
#       4! = 24
#       5! = 120
#
#   Victor Manuel Andreu Felipe 2025

# cálculo del factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# iteración para mostrar los factoriales
def show_factos(tope):
    for i in range(tope + 1):
        print(f"{i}! = {factorial(i)}")

while True:
    # control de input
    try:
        numero = int(input("Introduce un número entre 0 y 400: "))
        if 0 <= numero <= 400:
            break
        else:
            print("Por favor, introduce un número en el rango válido (0-400).")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

show_factos(numero)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   6.- Escribir un programa que solicite un número n y a continuación imprima todos los números
#   primos comprendidos en el intervalo [2-n]. El programa debe tener una función es_primo que
#   dado un número devuelva si el número es o no primo. Ejemplo:
#       Introduzca un número: 100
#       Números primos [2-100]: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97
#
#   Victor Manuel Andreu Felipe 2025

# funcion para saber si el número es primo
# usamos solo hasta la raíz cuadrada del número para ahorrar iteraciones
# puesto que al llegar ahí ya se han comprobado los pares
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# muestra todos los numeros primos entre 2 y n
def buscar_primos(n):
    primos = [str(num) for num in range(2, n + 1) if es_primo(num)]
    print(f"Números primos [2-{n}]: {', '.join(primos[:-1])} y {primos[-1]}" if primos else "No hay números primos en el rango.")

# control de input
while True:
    try:
        n = int(input("Introduzca un número: "))
        if n >= 2:
            break
        else:
            print("Por favor, introduce un número mayor o igual a 2.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

buscar_primos(n)

```

<div style="page-break-after: always;"></div>

```python
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


```


<div style="page-break-after: always;"></div>

```python
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

```

<div style="page-break-after: always;"></div>



```python
#!/usr/bin/python
#   9.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
#   de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
#   Monedas: 2 €, 1 €. El programa debe tener una lista con los billetes y monedas de curso legal.
#   Ejemplo:
#       Introduzca una cantidad: 2343
#       4 billetes de 500
#       1 billete de 200
#       1 billete de 100
#       2 billetes de 20
#       1 moneda de 2
#       1 moneda de 1
#
#   Victor Manuel Andreu Felipe 2025

def calcular_cambio(cantidad):
    # definimos los billetes/monedas
    billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    resultado = []
    
    # iteramos hasta llegar a 1
    for valor in billetes_monedas:
        cantidad_billetes = cantidad // valor  # calculamos la cantidad
        if cantidad_billetes > 0:
            tipo = "billete" if valor >= 5 else "moneda"
            plural = "s" if cantidad_billetes > 1 else ""
            # preparamos la cadena
            resultado.append(f"{cantidad_billetes} {tipo}{plural} de {valor}€") 
            cantidad %= valor  # actualizamos la cantidad
    
    return resultado

# control de input
while True:
    try:
        cantidad = int(input("Introduzca una cantidad en euros: ").strip())
        if cantidad >= 0:
            break
        else:
            print("Por favor, introduce una cantidad positiva.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

cambio = calcular_cambio(cantidad)
for linea in cambio:
    print(linea)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   10.- Escribe una función que dado el día, el mes y el año, devuelva un entero comprendido entre
#   1 y 366 indicando el número de día del año. La función tendrá esta declaración:
#      dia_agno(dia, mes, agno)
#
#   Victor Manuel Andreu Felipe 2025

# primero comprobamos si el año es bisiesto
def es_bisiesto(agno):
    return (agno % 4 == 0 and agno % 100 != 0) or (agno % 400 == 0)

def dia_agno(dia, mes, agno):
    # definimos los días de cada mes
    dias_por_mes = [31, 29 if es_bisiesto(agno) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # comprobación de fecha
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_por_mes[mes - 1]:
        raise ValueError("Fecha incorrecta")
    
    return sum(dias_por_mes[:mes - 1]) + dia


dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
agno = int(input("Introduce el año: "))

try:
    resultado = dia_agno(dia, mes, agno)
    print(f"El día {dia}/{mes}/{agno} corresponde al día {resultado} del año.")
except ValueError as e:
    print(e)

```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   11.- En Matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números
#   naturales:
#       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#   Podemos definirla más formalmente así:
#       f0 = 0
#       f1 = 1
#       fn = fn – 1 + fn – 2 para n = 2, 3, 4, 5 ...

#   Escribe un programa que calcule los 100 primeros términos de la sucesión y los almacene
#   en una lista, para calcular el siguiente término el programa debe basarse en los dos anteriores
#   previamente calculados. Una vez calculados, el programa debe mostrarlos en pantalla.
#
#   Victor Manuel Andreu Felipe 2025

def fibonacci(n):
    fib_seq = [0, 1]  # inicializamos la lista con los dos primeros valores
    
    # iteramos para calcular el siguiente valor sumando los dos últimos
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq

# Generamos y mostramos los 100 primeros números de Fibonacci
fibonacci_100 = fibonacci(100)

print("Sucesión de Fibonacci (100 términos):")
for i, num in enumerate(fibonacci_100):
    print(f"F({i}) = {num}")
```



<div style="page-break-after: always;"></div>
