#!/usr/bin/python

# Ejercicio 04:
# Modifica el programa anterior para que la foto se pueda mover en todas direcciones y que vaya
# rebotando por toda la pantalla.
#
#   Victor Manuel Andreu Felipe 2025

import pygame
import sys
import random

# dimensiones de la ventana
window_x = 800
window_y = 600

pygame.init()

# Configurar la ventana
window = pygame.display.set_mode((window_x, window_y))
window.fill((255, 255, 255))

# cargar la imagen
cara = pygame.image.load("cara.jpg")
cara_rect = cara.get_rect()

# posición inicial y velocidad
x = random.randint(0, window_x - cara_rect.width)
y = random.randint(0, window_y - cara_rect.height)
speed_x = 4
speed_y = 3

# Bucle principal
running = True
while running:
    pygame.time.delay(30)  # segundo control de velocidad

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    x += speed_x
    y += speed_y

    if x + cara_rect.width > window_x or x < 0:
        speed_x = -speed_x

    if y + cara_rect.height > window_y or y < 0:
        speed_y = -speed_y

    window.blit(cara, (x, y))
    pygame.display.flip()

pygame.quit()
sys.exit()