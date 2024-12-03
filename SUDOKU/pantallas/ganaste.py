import pygame
from botones import dibujar_boton_nueva_partida
from botones import dibujar_boton_ver_puntajes


def dibujar_pantalla_ganaste(pantalla, ancho_pantalla, largo_pantalla):
    pantalla.fill((50, 50, 50))  # Fondo gris oscuro
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_pausa = fuente.render("¡Ganaste!", True, (255, 255, 255))
    texto_x = ancho_pantalla // 2 - texto_pausa.get_width() // 2
    texto_y = largo_pantalla // 2 - texto_pausa.get_height() // 2
    dibujar_boton_nueva_partida(pantalla)
    dibujar_boton_ver_puntajes(pantalla)
    pantalla.blit(texto_pausa, (texto_x, texto_y))