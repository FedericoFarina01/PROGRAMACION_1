import pygame

def dibujar_botones_inicio(pantalla_inicio, img_inicio, texto_jugar, texto_puntajes, texto_salir):
    pantalla_inicio.fill((255, 255, 255))  # Llena la pantalla de un color de fondo
    pantalla_inicio.blit(img_inicio, (0, 0))  # Imagen de fondo

    # Botón Jugar
    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 90 - 2 , 135 + 4, 80 + 4), border_radius=15)
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 90, 135, 80), border_radius=15)
    pantalla_inicio.blit(texto_jugar, (300, 100))

    # Botón Puntajes
    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 240 - 2 , 190 + 4, 80 + 4), border_radius=15)
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 240, 190, 80), border_radius=10)
    pantalla_inicio.blit(texto_puntajes, (300, 250))

    # Botón Salir

    pygame.draw.rect(pantalla_inicio, (46, 134, 193), (290 - 2, 390 - 2 , 125 + 4, 80 + 4), border_radius=15)
    pygame.draw.rect(pantalla_inicio, (255, 255, 255), (290, 390, 125, 80), border_radius=10)
    pantalla_inicio.blit(texto_salir, (300, 400))


def dibujar_boton_volver(pantalla):
    x = 10
    y = 10
    ancho = 100
    alto = 40

    rect_volver = pygame.Rect(x, y, ancho, alto)  # Crear el rectángulo del botón
    pygame.draw.rect(pantalla, (46, 134, 193), (x - 2, y - 2, ancho + 4, alto + 4), border_radius=10)  # Borde
    pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto), border_radius=10)  # Fondo
    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    texto_volver = fuente.render("Volver", True, (0, 0, 0))
    pantalla.blit(texto_volver, (x + 20, y + 10))

    return rect_volver



#-------------------------------------------------------