# Practica 6. Introducción a Python

```python
#!/usr/bin/python

#   1.- Escribe un programa que muestre tu nombre en pantalla.
#
#   Víctor Manuel Andreu Felipe 2025

print("Víctor Manuel Andreu Felipe")
```

<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python

#   2.- Escribe un programa que pida una cadena y muestre una respuesta:
# Estás bajo mi control, harás lo que yo te diga.
# Sí... ¡¡ oh gran maestro !! Espero tus órdenes...
#
#   Víctor Manuel Andreu Felipe 2025

input("Se que puedes leerme el pensamiento, Bart: ")
print("Miau, Miau, Miau, Miau, Miau, Miau, Miau, ")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   3.- Escribe un programa que pregunte por tu nombre, por tu primer apellido y por tu segundo apellido.
#    A continuación imprimirá tu nombre de dos maneras:
#       ¿Cuál es tu nombre? José Antonio
#       ¿Y tu primer apellido? Sánchez
#       ¿Y tu segundo apellido? Pérez
#       Te llamas: José Antonio Sánchez Pérez
#       En las listas aparecerías como: Sánchez Pérez, José Antonio
#
#   Víctor Manuel Andreu Felipe 2025

nombre = input("¿Cuál es tu nombre? ")
apel1 = input("¿Y tu primer apellido? ")
apel2 = input("¿Y tu segundo apellido? ")

print("Te llamas:", nombre, apel1, apel2)
print("En las listas aparecerías como:", apel1, apel2, nombre)
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   4.- Escribe un programa que pregunte por tu nombre y por tu edad, a continuación debe mostrar la siguiente cadena:
#       ¿Cuál es tu nombre? Ana
#       ¿Cuántos años tienes? 24
#       ¡ Hola Ana, es un placer hablar contigo !
#       ¡¡ Te conservas muy bien para tener solo 24 años !!
#
#   Víctor Manuel Andreu Felipe 2025

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")

print("¡ Hola,", nombre, ",es un placer hablar contigo !")
print("¡¡ Te conservas muy bien para tener solo",edad,"años !!")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   5.- Escribir un programa que pida un número de 2 cifras, a continuación debe mostrar el número al revés. Ejemplo:
#       Dame un número: 24
#       El número al revés es: 42
#
#   Víctor Manuel Andreu Felipe 2025

numero = int(input("Dame un número: "))     # convertimos a int para hacer operaciones
decenas = int(numero / 10)                  # convertimos el resultado a int para que no de decimales
unidades = numero % 10

print("El número al revés es: ", unidades, decenas, sep='')
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   6.- Mejora el programa para que no acepte ni números menores de 10 ni mayores de 99.
#       Ejemplo:
#           Dame un número: 8
#           El número 8 no me sirve, tiene que ser mayor o igual que 10.
#
#   Víctor Manuel Andreu Felipe 2025
#
#   No he sido capaz de hacerlo sin condicionales. Suponiendo que sabemos usar condicionales, el código quedaría así:

numero = int(input("Dame un número: "))     # convertimos a int para hacer operaciones

if numero < 10 or numero > 99:
    print("El número", numero, "no me sirve, tiene que ser mayor o igual que y menor o igual que 99")
else:
    decenas = int(numero / 10)                  # convertimos el resultado a int para que no de decimales
    unidades = numero % 10

    print("El número al revés es: ", unidades, decenas, sep='')
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
# 7.- Escribe un programa que pida una cantidad en euros, a continuación mostrará la cantidad en pesetas (recordamos que 1€ = 166'386 pesetas):
#   Dame una cantidad (en €): 20
#   La peseta ha desaparecido :(, pero:
#   20 € eran 3328 pesetas.
#
#   Víctor Manuel Andreu Felipe 2025

euros = float(input("Dame una cantidad (en €): "))      # convertimos a float para poder indicarle una cantidad fraccional.

pesetas = euros * 166.386

print("La peseta ha desaparecido :(, pero: ")
print(euros, "€ eran", pesetas, "pesetas.")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
# 8.- Escribe un programa que calcule la superficie de un cuadrado, para ello tiene que pedir la longitud del lado:
#   Vamos a calcular la superficie de un cuadrado...
#   ¿Cuánto mide el lado (en cm): 20
#   La superficie del cuadrado es de 400 cm^2.
#
#   Víctor Manuel Andreu Felipe 2025

lado = float(input("¿Cuánto mide el lado (en cm): "))

area = lado * lado

print("La superficie del cuadrado es de", area, "cm^2.")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   9.- Escribe un programa que calcule la superficie de un triángulo, para ello tiene que pedir la longitud de la base y de la altura:
#       Vamos a calcular la superficie de un triángulo...
#       ¿Cuánto mide de base (en cm): 21
#       ¿Cuánto mide de altura (en cm): 17
#       La superficie del triángulo es de 178.5 cm^2.
#
#   Víctor Manuel Andreu Felipe 2025

base = float(input("¿Cuánto mide de base (en cm): "))
altura = float(input("¿Cuánto mide de altura (en cm): "))

area = base * altura / 2

print("La superficie del triángulo es de", area, "cm^2.")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#  10.- Escribe un programa que calcule potencias para un número dado. El programa debe pedir un
#   número y a continuación calcular el cuadrado, el cubo, la potencia cuarta y la potencia quinta. En
#   Python se puede calcular el cubo de un número de dos formas:
#       x * x * x
#       x ** 3
#   Ejemplo:
#       Dame un número: 3
#       3 ^ 2 = 9
#       3 ^ 3 = 27
#       3 ^ 4 = 81
#       3 ^ 5 = 243
#
#   Víctor Manuel Andreu Felipe 2025

numero = int(input("Dame un número: "))

print(numero, "^ 2 =", numero ** 2)
print(numero, "^ 3 =", numero ** 3)
print(numero, "^ 4 =", numero ** 4)
print(numero, "^ 5 =", numero ** 5)
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   11.- Escribe un programa que calcule la longitud de una circunferencia. El programa debe pedir el
#   radio y a continuación calcular la longitud. Podemos tomar el valor de pi desde el módulo
#   (librería ) math. Así:
#   import math
#   ...
#       print(math.pi)
#   Ejemplo:
#       Dame el radio (en cm por favor): 3
#       La longitud de la O es: 18.8495559215 cm
#
#   Víctor Manuel Andreu Felipe 2025

import math

radio = float(input("Dame el radio (en cm por favor): "))

circun = 2 * math.pi * radio

print("La longitud de la O es:", circun, "cm")
```
<div style="page-break-after: always;"></div>

```python
#!/usr/bin/python
#
#   12.- Escribe un programa que calcule el tiempo que se tarda en llegar a un sitio dada la velocidad
#   y la distancia.
#       Me falla el GPS :( ¿Dónde estamos? Murcia
#       ¿A dónde vamos? Madrid
#       ¿A qué velocidad? 100
#       ¿Te sabes la distancia? 398
#       A 100 Km/h tardaríamos 3.98 horas
#       A 120 Km/h tardaríamos 3.32 horas, pero mejor no correr mucho :)
#
#   Víctor Manuel Andreu Felipe 2025

input("Me falla el GPS :( ¿Dónde estamos? ")
input("¿A dónde vamos? ")
velo = float(input("¿A qué velocidad? "))
dist = float(input("¿Te sabes la distancia? "))

print("A", velo, "Km/h tardaríamos", dist / velo, "horas")
print("A 120 Km/h tardaríamos", dist / 120, "horas, pero mejor no correr mucho :)")
```