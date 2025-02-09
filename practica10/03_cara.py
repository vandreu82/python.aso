#!/usr/bin/python

# Ejercicio 03:
# Cambia el icono de la pantalla por una foto de tu cara, tomada con el móvil o con una webcam.
# Haz que tu cara vaya moviéndose en pantalla de izquierda a derecha, cuando llegue a uno de los
# extremos salga rebotada hacia el extremo contrario.
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

# cargar la imagen
cara = pygame.image.load("cara.jpg")
cara_rect = cara.get_rect() # crea un marco

# posición inicial y velocidad
x = random.randint(0, window_x - cara_rect.width)
y = random.randint(0, window_y - cara_rect.height)
speed_x = 5

running = True
while running:
    pygame.time.delay(40)  # segundo control de velocidad

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    window.fill((255, 255, 255)) # limpiamos porque si no deja surco
    x += speed_x
    
    # condicional para que cuando toca un borde de la vuelta
    if x + cara_rect.width > window_x or x < 0:
        speed_x = -speed_x

    window.blit(cara, (x, y))
    pygame.display.flip()
    
pygame.quit()
sys.exit()