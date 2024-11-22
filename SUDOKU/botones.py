import pygame

def dibujar_boton_volver(pantalla):
    x = 10
    y = 10
    ancho = 100
    alto = 40

    pygame.draw.rect(pantalla, (46, 134, 193), (x - 2, y - 2, ancho + 4, alto + 4), border_radius=10)  # Borde
    rect_volver = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto), border_radius=10)
    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    texto_volver = fuente.render("Volver", True, (0, 0, 0))
    pantalla.blit(texto_volver, (x + 20, y + 10))

    return rect_volver



#-------------------------------------------------------
def dibujar_boton_jugar(pantalla):
    x = 290
    y = 90
    ancho = 135
    alto = 80

    pygame.draw.rect(pantalla, (46, 134, 193), (x - 2, y - 2 , ancho + 4, alto + 4), border_radius=15) # Borde
    rect_jugar = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto), border_radius=15)
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
    pantalla.blit(texto_jugar, (x + 15, y + 10))

    return rect_jugar


def dibujar_boton_puntajes(pantalla):
    x = 290
    y = 240
    ancho = 190
    alto = 80

    pygame.draw.rect(pantalla, (46, 134, 193), (x - 2, y - 2 , ancho + 4, alto + 4), border_radius=15) # Borde
    rect_puntajes = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto), border_radius=10)
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
    pantalla.blit(texto_puntajes, (x + 15, y + 10))

    return rect_puntajes


def dibujar_boton_salir(pantalla):
    x = 290
    y = 390
    ancho = 125
    alto = 80

    pygame.draw.rect(pantalla, (46, 134, 193), (x - 2, y - 2 , ancho + 4, alto + 4), border_radius=15) # Borde
    rect_salir = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto), border_radius=10)
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_salir = fuente.render("Salir", True, (0, 0, 0))
    pantalla.blit(texto_salir, (x + 15, y + 10))

    return rect_salir
