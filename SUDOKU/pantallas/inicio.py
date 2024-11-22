import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

# Cargar imágenes
img_inicio = pygame.image.load("SUDOKU/imagenes/img_fondo_inicio.png")
img_inicio = pygame.transform.scale(img_inicio, dimension_pantalla)

def dibujar_pantalla_inicio(pantalla):
    pantalla.fill((255, 255, 255))
    pantalla.blit(img_inicio, (0, 0))
    dibujar_boton_jugar(pantalla)
    dibujar_boton_puntajes(pantalla)
    dibujar_boton_salir(pantalla)