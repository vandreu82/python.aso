#!/usr/bin/python

# Ejercicio 01:
#   1.- Dibuje 20 círculos aleatorios.
#   2.- Dibuje un solo círculo en mitad de la pantalla con un radio igual a la mitad del tamaño
#   de la ventana.
#
#   Victor Manuel Andreu Felipe 2025

import pygame
import sys
import random

# dimensiones de la ventana
window_x = 640
window_y = 480

pygame.init()

# preparar la ventana
window = pygame.display.set_mode((window_x, window_y))
window.fill((255, 255, 255))

# dibujar 20 círculos aleatorios
for _ in range(20):
    x = random.randint(0, window_x)
    y = random.randint(0, window_y)
    radio = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(window, color, (x, y), radio)

center_radio = min(window_x, window_y) // 2

# dibujar un círculo negro en el centro con borde 2 pixeles(, 2) y sin relleno
pygame.draw.circle(window, [ 0, 0, 0 ], [ window_x / 2, window_y / 2 ], center_radio, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()