import pygame

# Inicializamos pygame
pygame.init() 


# Tamaños y ubicaciones: X, Y 
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)


# Creacion de una pantallas con sus dimensiones
pantalla_inicio = pygame.display.set_mode(dimension_pantalla)
pantalla_principal = pygame.display.set_mode(dimension_pantalla)
pantalla_puntajes = pygame.display.set_mode(dimension_pantalla)

img_inicio = pygame.image.load("SUDOKU/imagenes/img_fondo_inicio.png") # Imagen de fondo de incio
img_inicio = pygame.transform.scale(img_inicio, (800, 600)) # Ajustar el tamaño de la imagen

#img_puntajes = pygame.image.load("") # Imagen de fondo de incio
#img_puntajes = pygame.transform.scale(img_puntajes, (800, 600)) # Ajustar el tamaño de la imagen


# Texto inicio
fuente = pygame.font.SysFont("Arial", 50, bold = True)
texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
texto_salir = fuente.render("Salir", True, (0, 0, 0))

jugar_rect = texto_jugar.get_rect()


# Cambia el titulo del juego
pygame.display.set_caption("Sudoku") 


# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono) 


juego_corriendo = True

while juego_corriendo == True:  

    # (Iteramos sobre todos los eventos del juego)
    lista_eventos = pygame.event.get() 
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # Preguntamos si el usuario apreto la cruz para cerrar el juego.
            juego_corriendo = False # B
            pygame.quit() # Cerramos el juego.
            quit()
            

    pantalla_inicio.fill((255, 255, 255)) # Llena la pantalla de un color de fondo.
    pantalla_principal.fill((255, 255, 255))
    pantalla_puntajes.fill((255, 255, 255))


    pantalla_inicio.blit(img_inicio, (0, 0))

    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 90 - 2 , 135 + 4, 80 + 4), border_radius=15) # Borde
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 90, 135, 80), border_radius=15)
    pantalla_inicio.blit(texto_jugar, (300, 100))

    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 240 - 2 , 190 + 4, 80 + 4), border_radius=15) # Borde
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 240, 190, 80), border_radius=10)
    pantalla_inicio.blit(texto_puntajes, (300, 250))

    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 390 - 2 , 125 + 4, 80 + 4), border_radius=15) # Borde
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 390, 125, 80), border_radius=15)
    pantalla_inicio.blit(texto_salir, (300, 400))

    pygame.display.flip() # Siempre actualiza toda la pantalla (Siempre al final del bucle)