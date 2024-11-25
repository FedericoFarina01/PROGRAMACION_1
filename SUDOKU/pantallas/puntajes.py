import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)


img_fondo = pygame.image.load("SUDOKU/imagenes/marco.jpg")
img_fondo = pygame.transform.scale(img_fondo, (1000, 800))

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

def dibujar_pantalla_puntajes(pantalla):
    pantalla.fill((255, 255, 255))  
    pantalla.blit(img_fondo, (-100, -100))
    dibujar_boton_volver(pantalla) 
    dibujar_top_5(pantalla)


def dibujar_top_5(pantalla):
    dibujar_titulos_top(pantalla)
    dibujar_top_5_rankings(pantalla)
    dibujar_top_5_users(pantalla)
    dibujar_top_5_puntos(pantalla)

def dibujar_titulos_top(pantalla):
    fuente_titulos = pygame.font.SysFont("Arial", 40, bold=True)
    texto_rank = fuente_titulos.render("RANK", True, (0, 0, 0))
    texto_user = fuente_titulos.render("USER", True, (0, 0, 0))
    texto_puntos = fuente_titulos.render("PUNTOS", True, (0, 0, 0))
    pantalla.blit(texto_rank, (200, 100))
    pantalla.blit(texto_user, (350, 100))
    pantalla.blit(texto_puntos, (500, 100))


def dibujar_top_5_rankings(pantalla):
    dibujar_ranking(pantalla, "1.", 240, 200)
    dibujar_ranking(pantalla, "2.", 240, 270)
    dibujar_ranking(pantalla, "3.", 240, 345)
    dibujar_ranking(pantalla, "4.", 240, 420)
    dibujar_ranking(pantalla, "5.", 240, 495)


def dibujar_ranking(pantalla, ranking, x, y):
    fuente_ranking = pygame.font.SysFont("Arial", 40, bold=True)
    texto_ranking = fuente_ranking.render(ranking, True, (0, 0, 0))
    pantalla.blit(texto_ranking, (x, y))


def dibujar_top_5_users(pantalla):
    dibujar_user(pantalla, "Primero", 350, 206)
    dibujar_user(pantalla, "Segundo", 350, 276)
    dibujar_user(pantalla, "Tercero", 350, 351)
    dibujar_user(pantalla, "Cuarto", 350, 426)
    dibujar_user(pantalla, "Quinto", 350, 501)


def dibujar_user(pantalla, user, x, y):
    fuente_user = pygame.font.SysFont("Arial", 30, bold=True)
    texto_user = fuente_user.render(user, True, (0, 0, 0))
    pantalla.blit(texto_user, (x, y))


def dibujar_top_5_puntos(pantalla):
    dibujar_puntos(pantalla, "1000", 540, 206)
    dibujar_puntos(pantalla, "2000", 540, 276)
    dibujar_puntos(pantalla, "3000", 540, 351)
    dibujar_puntos(pantalla, "4000", 540, 426)
    dibujar_puntos(pantalla, "5000", 540, 501)


def dibujar_puntos(pantalla, puntos, x, y):
    fuente_puntos = pygame.font.SysFont("Arial", 30, bold=True)
    texto_puntos = fuente_puntos.render(puntos, True, (0, 0, 0))
    pantalla.blit(texto_puntos, (x, y))

