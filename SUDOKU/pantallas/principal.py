import pygame
from botones import *
from funciones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

img_fondo = pygame.image.load("SUDOKU/imagenes/marco.jpg")
img_fondo = pygame.transform.scale(img_fondo, (1000, 800))

matriz_sudoku = generar_tablero_sudoku(9, 9, 0, 0, 8)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

def dibujar_pantalla_principal(pantalla, tiempo_inicio, cant_errores):
    pantalla.blit(img_fondo, (-100, -100))
    dibujar_boton_volver(pantalla) 
    dibujar_boton_reiniciar(pantalla)
    dibujar_boton_pausa(pantalla)
    dibujar_errores(pantalla, cant_errores)
    dibujar_tiempo(pantalla, tiempo_inicio)
    dibujar_matriz_sudoku(pantalla, matriz_sudoku)
   # pygame.mixer.music.stop()



#--------------------------------------------------------------------------------
# Dibujar SUDOKU en Pygame

def dibujar_matriz_sudoku(pantalla, matriz):
    """
    Dibuja la matriz de Sudoku en la pantalla de Pygame.

    Parámetros:
        pantalla: La pantalla de Pygame donde se dibujará.
        matriz: La matriz de Sudoku que se debe mostrar.
    """
    # Colores
    color_linea = (0, 0, 0)
    color_numeros= (0, 0, 0)  # Negro para los números
    
    # Coordenadas de inicio y tamaño de celdas
    inicio_x = 150
    inicio_y = 60
    tamaño_celda = 55 # Cada celda será de 50x50 píxeles

    # Dibujar la cuadrícula (líneas horizontales y verticales)
    for fila in range(10):  # Dibujar 9 líneas más una extra para el borde
        grosor = 3 if fila % 3 == 0 else 1  # Líneas más gruesas cada 3

        pygame.draw.line(pantalla, (color_linea), (inicio_x, inicio_y + fila * tamaño_celda), 
                         (inicio_x + 9 * tamaño_celda, inicio_y + fila * tamaño_celda), 
                         grosor)
        
        pygame.draw.line(pantalla, (color_linea), 
                         (inicio_x + fila * tamaño_celda, inicio_y), 
                         (inicio_x + fila * tamaño_celda, inicio_y + 9 * tamaño_celda), 
                         grosor)

    # Dibujar los números en la cuadrícula
    fuente = pygame.font.SysFont("Arial", 30)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numeros = fuente.render(str(matriz[i][j]), True, color_numeros)
            x = inicio_x + j * tamaño_celda + tamaño_celda // 3
            y = inicio_y + i * tamaño_celda + tamaño_celda // 4
            pantalla.blit(numeros, (x, y))

#--------------------------------------------------------------------------------------