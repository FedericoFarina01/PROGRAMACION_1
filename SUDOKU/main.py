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

# Texto botones inicio
fuente = pygame.font.SysFont("Arial", 50, bold=True)
texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
texto_salir = fuente.render("Salir", True, (0, 0, 0))

# Cambia el título del juego
pygame.display.set_caption("Sudoku")

# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono)

# Variables de estado
juego_corriendo = True
pantalla_activa = "inicio"  # Puede ser "inicio", "principal", o "puntajes"

while juego_corriendo:
    # Iterar sobre todos los eventos
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            juego_corriendo = False
            pygame.quit()
            quit()

        # Detectar clics del ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            # Detectar clic en el botón "Jugar"
            if pantalla_activa == "inicio" and 290 <= x <= 425 and 90 <= y <= 170: # HAY QUE USAR EL METODO DE COLISION CON EL RECTANGULO DEL BOTON COMO VIMOS EN CLASE
                pantalla_activa = "principal" 

            # Detectar clic en el botón "Puntajes"
            if pantalla_activa == "inicio" and 290 <= x <= 480 and 240 <= y <= 320:
                pantalla_activa = "puntajes"

            if pantalla_activa == "inicio" and 290 <= x <= 415 and 390 <= y <= 470:
                juego_corriendo = False  # Terminar el bucle principal
                pygame.quit()
                quit()

            # Detectar clic en el botón "Volver"
            rect_volver = dibujar_boton_volver(pantalla)
            if rect_volver.collidepoint(x, y):
                pantalla_activa = "inicio"


    # Dibujar pantalla INICIO
    if pantalla_activa == "inicio":
        pantalla.fill((255, 255, 255))
        pantalla.blit(img_inicio, (0, 0))
        dibujar_botones_inicio(pantalla, img_inicio, texto_jugar, texto_puntajes, texto_salir)

    # Dibujar pantalla PRINCIPAL
    elif pantalla_activa == "principal":
        pantalla.fill((255, 255, 255)) 
        dibujar_boton_volver(pantalla)  # Dibujar el botón "Volver"
        if pygame.mouse.get_pos() == rect_volver:
                pantalla_activa = "inicio"

    # Dibujar pantalla PUNTAJES
    elif pantalla_activa == "puntajes":
        pantalla.fill((255, 255, 255))  
        pantalla.blit(img_puntajes, (0, 0))
        rect_volver = dibujar_boton_volver(pantalla)  # Dibuja y obtiene el rectángulo
        if pygame.mouse.get_pos() == rect_volver:
                pantalla_activa = "inicio"
    
    pygame.display.flip()  # Actualiza la pantalla
