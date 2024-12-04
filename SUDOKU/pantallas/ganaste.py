import pygame


def dibujar_pantalla_ganaste(pantalla, cant_errores, minutos, dificultad, puntaje_base):

    if dificultad == "Facil":
        bonus_dificultad = 1.25
    elif dificultad == "Medio":
        bonus_dificultad = 1.5
    elif dificultad == "Dificil":
        bonus_dificultad = 1.75

    # Calcular el puntaje final
    puntaje_final = (puntaje_base - (cant_errores * 50) - (minutos * 10)) * bonus_dificultad

    # Fondo y título
    pantalla.fill((50, 50, 50))  # Fondo gris oscuro
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_ganaste = fuente.render("¡Ganaste!", True, (255, 255, 255))

    # Dibuja los botones
    dibujar_boton_nueva_partida(pantalla)  # Botón "Nueva Partida"
    dibujar_boton_ver_puntajes(pantalla)  # Botón "Ver Puntajes"

    # Mostrar el puntaje final
    fuente_puntos = pygame.font.SysFont("Arial", 40, bold=True)
    texto_puntajes = fuente_puntos.render(f"Puntos: {int(puntaje_final)}", True, (0, 0, 0))
    pantalla.blit(texto_puntajes, (265, 200))

    # Mostrar el título
    pantalla.blit(texto_ganaste, (280, 30))


def dibujar_boton_nueva_partida(pantalla):
    """
    Dibuja el boton reanudar en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_nueva_partida: Representa el area del boton reanudar
    """
    x = 10
    y = 30
    ancho = 200
    alto = 40

    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_nueva_partida = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_nueva_partida = fuente.render("Nueva partida", True, (0, 0, 0))
    pantalla.blit(texto_nueva_partida, (x + 20, y + 5))
    
    return rect_nueva_partida

def dibujar_boton_ver_puntajes(pantalla):
    """
    Dibuja el boton reanudar en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_ver_puntajes: Representa el area del boton reanudar
    """
    x = 600
    y = 30  
    ancho = 200
    alto = 40
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_ver_puntajes = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_ver_puntajes = fuente.render("Ver puntajes", True, (0, 0, 0))
    pantalla.blit(texto_ver_puntajes, (x + 20, y + 5))
    
    return rect_ver_puntajes
