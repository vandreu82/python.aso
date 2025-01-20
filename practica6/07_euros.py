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