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