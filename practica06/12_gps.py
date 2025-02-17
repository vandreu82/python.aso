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