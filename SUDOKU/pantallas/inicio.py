import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

# Cargar imágenes
img_pygame = pygame.image.load("SUDOKU/imagenes/pygame.png")
img_pygame = pygame.transform.scale(img_pygame, (400, 250))

img_sudoku = pygame.image.load("SUDOKU/imagenes/sudoku.png")
img_sudoku = pygame.transform.scale(img_sudoku, (150, 50))

def dibujar_pantalla_inicio(pantalla, dificultad, nombre_jugador):
    pantalla.fill((255, 255, 255))  # Fondo blanco
    pantalla.blit(img_pygame, (160, 0))
    pantalla.blit(img_sudoku, (530, 130))
    # Dibujar botones
    dibujar_boton_jugar(pantalla)
    dibujar_boton_dificultad(pantalla, dificultad)
    dibujar_boton_puntajes(pantalla)
    dibujar_boton_salir(pantalla)
    
    # Dibujar el campo de texto para ingresar el nombre del jugador
    dibujar_boton_nombre(pantalla, nombre_jugador)





