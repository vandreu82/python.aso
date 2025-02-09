#!/usr/bin/python

# Ejercicio 02:
# Modifica el programa para que dibuje rectángulos aleatorios:
#  - De un mismo color.
#  - De colores aleatorios.
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

# dibujar rectángulos aleatorios de un mismo color (verde)
for _ in range(10):
    x = random.randint(0, window_x)
    y = random.randint(0, window_y)
    base = random.randint(20, 100)
    altura = random.randint(20, 100)
    color = (0, 255, 0)
    pygame.draw.rect(window, color, (x, y, base, altura))

# dibujar rectángulos aleatorios de colores aleatorios
for _ in range(10):
    x = random.randint(0, window_x)
    y = random.randint(0, window_y)
    base = random.randint(20, 100)
    altura = random.randint(20, 100)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(window, color, (x, y, base, altura))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()