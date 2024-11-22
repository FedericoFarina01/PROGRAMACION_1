import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)


img_puntajes = pygame.image.load("SUDOKU/imagenes/puntajes.jpg")
img_puntajes = pygame.transform.scale(img_puntajes, dimension_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

def dibujar_pantalla_puntajes(pantalla):
    pantalla.fill((255, 255, 255))  
    pantalla.blit(img_puntajes, (0, 0))
    dibujar_boton_volver(pantalla) 