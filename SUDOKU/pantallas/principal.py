import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

def dibujar_pantalla_principal(pantalla):
    pantalla.fill((255, 255, 255))  
    dibujar_boton_volver(pantalla) 