import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

pygame.font.init() 
fuente = pygame.font.SysFont("Arial", 32)

# Cargar imágenes
img_pygame = pygame.image.load("SUDOKU/imagenes/pygame.png")
img_pygame = pygame.transform.scale(img_pygame, (400, 250))

img_sudoku = pygame.image.load("SUDOKU/imagenes/sudoku.png")
img_sudoku = pygame.transform.scale(img_sudoku, (150, 50))

def dibujar_pantalla_inicio(pantalla):
    pantalla.fill((255, 255, 255))
    pantalla.blit(img_pygame, (160, 0))
    pantalla.blit(img_sudoku, (530, 130 ))
    dibujar_boton_jugar(pantalla)
    dibujar_boton_dificultad(pantalla)
    dibujar_boton_puntajes(pantalla)
    dibujar_boton_salir(pantalla)
#----------------------------------------------------------------------------------------




