#!/usr/bin/python

# Ejercicio 05:
# Modifica el anterior programa para que en vez de una cara rebotando por la pantalla sean dos
# caras rebotando por la pantalla.
#
#   Victor Manuel Andreu Felipe 2025

import pygame
import sys
import random

# dimensiones de la ventana
window_x = 800
window_y = 600

pygame.init()

# preparar la ventana
window = pygame.display.set_mode((window_x, window_y))
window.fill((255, 255, 255))  # Fondo blanco

# cargar la imagen
cara = pygame.image.load("cara.jpg")
cara_rect = cara.get_rect()

# posiciones iniciales y velocidades
caras = [
    {"x": random.randint(0, window_x - cara_rect.width), 
     "y": random.randint(0, window_y - cara_rect.height), 
     "speed_x": 4, 
     "speed_y": 3},
    {"x": random.randint(0, window_x - cara_rect.width),
     "y": random.randint(0, window_y - cara_rect.height),
     "speed_x": 4,
     "speed_y": 5}
]

running = True
while running:
    pygame.time.delay(30)  # segundo control de velocidad

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    for cara_obj in caras:
        cara_obj["x"] += cara_obj["speed_x"]
        cara_obj["y"] += cara_obj["speed_y"]

        # condicionales para rebotar
        if cara_obj["x"] + cara_rect.width > window_x or cara_obj["x"] < 0:
            cara_obj["speed_x"] = -cara_obj["speed_x"]

        if cara_obj["y"] + cara_rect.height > window_y or cara_obj["y"] < 0:
            cara_obj["speed_y"] = -cara_obj["speed_y"]

        window.blit(cara, (cara_obj["x"], cara_obj["y"]))
        
    pygame.display.flip()

pygame.quit()
sys.exit()