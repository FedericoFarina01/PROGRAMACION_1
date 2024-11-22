import pygame
from funciones import *
from botones import *

# Inicializamos pygame
pygame.init()

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

# Cargar imágenes
img_inicio = pygame.image.load("SUDOKU/imagenes/img_fondo_inicio.png")
img_inicio = pygame.transform.scale(img_inicio, dimension_pantalla)

img_puntajes = pygame.image.load("SUDOKU/imagenes/puntajes.jpg")
img_puntajes = pygame.transform.scale(img_puntajes, dimension_pantalla)

# Cambia el título del juego
pygame.display.set_caption("Sudoku")

# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono)

# Variables
juego_corriendo = True
pantalla_activa = "inicio"
click_izq = pygame.MOUSEBUTTONDOWN

while juego_corriendo:
    # Iterar sobre todos los eventos
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            juego_corriendo = False
            pygame.quit()
            quit()

        # Detectar clics del ratón
        if evento.type == click_izq:
            x, y = evento.pos

            # Detectar clic en los botones de la pantalla de inicio
            if pantalla_activa == "inicio":
                rect_jugar = dibujar_boton_jugar(pantalla)
                rect_puntajes = dibujar_boton_puntajes(pantalla)
                rect_salir = dibujar_boton_salir(pantalla)

                if rect_jugar.collidepoint(x, y):
                    pantalla_activa = "principal"

                elif rect_puntajes.collidepoint(x, y):
                    pantalla_activa = "puntajes"

                elif rect_salir.collidepoint(x, y):
                    juego_corriendo = False
                    pygame.quit()
                    quit()

            # Detectar clic en el botón "Volver" en las pantallas "principal" o "puntajes"
            elif pantalla_activa == "principal":
                rect_volver = dibujar_boton_volver(pantalla)
                if rect_volver.collidepoint(x, y):
                    pantalla_activa = "inicio"

            elif pantalla_activa == "puntajes":
                rect_volver = dibujar_boton_volver(pantalla)
                if rect_volver.collidepoint(x, y):
                    pantalla_activa = "inicio"

    # Dibujar pantallas
    if pantalla_activa == "inicio":
        pantalla.fill((255, 255, 255))
        pantalla.blit(img_inicio, (0, 0))
        dibujar_boton_jugar(pantalla)
        dibujar_boton_puntajes(pantalla)
        dibujar_boton_salir(pantalla)

    elif pantalla_activa == "principal":
        pantalla.fill((255, 255, 255))  
        dibujar_boton_volver(pantalla) 

    elif pantalla_activa == "puntajes":
        pantalla.fill((255, 255, 255))  
        pantalla.blit(img_puntajes, (0, 0))
        dibujar_boton_volver(pantalla)  

    pygame.display.flip()  # Actualiza la pantalla
