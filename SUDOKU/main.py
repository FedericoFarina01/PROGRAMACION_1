import pygame

# Inicializamos pygame
pygame.init() 


# Tamaños y ubicaciones: X, Y 
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creacion de una pantalla con sus dimensiones
pantalla = pygame.display.set_mode(dimension_pantalla) 

# pantalla = pygame.display.set_mode(dimension_pantalla, pygame.RESIZABLE) # Pantalla de tamaño ajustable

# Cambia el titulo del juego
pygame.display.set_caption("Sudoku") 

# Icono del juego
pygame.display.set_icon() 

juego_corriendo = True

while juego_corriendo == True:  

    # (Iteramos sobre todos los eventos del juego)
    lista_eventos = pygame.event.get() 
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # Preguntamos si el usuario apreto la cruz para cerrar el juego.
            juego_corriendo = False # B
            pygame.quit() # Cerramos el juego.
            quit()
            

    pantalla.fill((118, 182, 184)) # Llena la pantalla de un color de fondo.
    
    pygame.display.flip() # Siempre actualiza toda la pantalla (Siempre al final del bucle)