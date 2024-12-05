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

def dibujar_pantalla_puntajes(pantalla,lista_puntajes):
    pantalla.fill((255, 255, 255))  
    pantalla.blit(img_fondo, (-100, -100))
    dibujar_boton_volver(pantalla) 
    dibujar_top_5(pantalla,lista_puntajes)


def dibujar_top_5(pantalla,lista_puntajes):
    if len(lista_puntajes) != 0:
        dibujar_titulos_top(pantalla)
        dibujar_top_5_rankings(pantalla,lista_puntajes)
        dibujar_top_5_users(pantalla,lista_puntajes)
        dibujar_top_5_puntos(pantalla,lista_puntajes)
    else:
        fuente_grande = pygame.font.SysFont("Arial", 60, bold=True)
        texto_puntos = fuente_grande.render("NO HAY PUNTAJES", True, (0, 0, 0))
        pantalla.blit(texto_puntos, (200, 100))

def dibujar_titulos_top(pantalla):
    fuente_titulos = pygame.font.SysFont("Arial", 40, bold=True)
    texto_rank = fuente_titulos.render("RANK", True, (0, 0, 0))
    texto_user = fuente_titulos.render("USER", True, (0, 0, 0))
    texto_puntos = fuente_titulos.render("PUNTOS", True, (0, 0, 0))
    pantalla.blit(texto_rank, (200, 100))
    pantalla.blit(texto_user, (350, 100))
    pantalla.blit(texto_puntos, (500, 100))


def dibujar_top_5_rankings(pantalla,lista_puntajes):
    valor_y = 200
    for i in range(len(lista_puntajes)):
        if i == 5:
            break
        dibujar_ranking(pantalla,str(i + 1),240,valor_y)
        valor_y += 75


def dibujar_ranking(pantalla, ranking, x, y):
    fuente_ranking = pygame.font.SysFont("Arial", 40, bold=True)
    texto_ranking = fuente_ranking.render(ranking, True, (0, 0, 0))
    pantalla.blit(texto_ranking, (x, y))


def dibujar_top_5_users(pantalla,lista_puntajes):
    valor_y = 206
    for i in range(len(lista_puntajes)):
        if i == 5:
            break
        dibujar_user(pantalla, lista_puntajes[i]["nombre"], 350, valor_y)
        valor_y += 75


def dibujar_user(pantalla, user, x, y):
    fuente_user = pygame.font.SysFont("Arial", 30, bold=True)
    texto_user = fuente_user.render(user, True, (0, 0, 0))
    pantalla.blit(texto_user, (x, y))


def dibujar_top_5_puntos(pantalla,lista_puntajes):
    valor_y = 206
    for i in range(len(lista_puntajes)):
        if i == 5:
            break
        dibujar_user(pantalla, str(lista_puntajes[i]["puntos"]), 540, valor_y)
        valor_y += 75



def dibujar_puntos(pantalla, puntos, x, y):
    fuente_puntos = pygame.font.SysFont("Arial", 30, bold=True)
    texto_puntos = fuente_puntos.render(puntos, True, (0, 0, 0))
    pantalla.blit(texto_puntos, (x, y))

