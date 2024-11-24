import pygame


def dibujar_boton_jugar(pantalla):
    x = 290
    y = 200
    ancho = 135
    alto = 80

    rect_jugar = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto))
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
    pantalla.blit(texto_jugar, (x + 15, y + 10))

    return rect_jugar

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_puntajes(pantalla):
    x = 290
    y = 270
    ancho = 135
    alto = 80

    rect_puntajes = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto))
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
    pantalla.blit(texto_puntajes, (x + 15, y + 10))

    return rect_puntajes
#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_dificultad(pantalla, dificultad):
    x = 290
    y = 340
    ancho = 190
    alto = 80

    rect_dificultad = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto))
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    texto_dificultad = fuente.render(dificultad, True, (0, 0, 0))
    pantalla.blit(texto_dificultad, (x + 15, y + 10))

    return rect_dificultad
#----------------------------------------------------------------------------------
def dibujar_boton_salir(pantalla):
    x = 290
    y = 410
    ancho = 125
    alto = 80

    rect_salir = pygame.draw.rect(pantalla, (255, 255, 255), (x, y, ancho, alto))
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    texto_salir = fuente.render("Salir", True, (0, 0, 0))
    pantalla.blit(texto_salir, (x + 15, y + 10))

    return rect_salir

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_volver(pantalla):
    imagen_volver = pygame.image.load("SUDOKU/imagenes/flecha_volver.png")
    imagen_volver = pygame.transform.scale(imagen_volver, (50, 50))  

    x = 10
    y = 10
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_volver, (x, y))
    
    return rect_volver

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_nombre(pantalla, nombre_jugador):

    x = 120
    y = 560
    ancho = 250
    alto = 30

    # Dibujar la caja de texto
    rect_nombre = pygame.draw.rect(pantalla, (0, 0, 0),(x, y, ancho, alto))  # Fondo caja nombre
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    texto_nombre = fuente.render(nombre_jugador, True, (0, 0, 0))
    fuente_etiqueta = pygame.font.SysFont("Arial", 30, bold=True)
    etiqueta = fuente_etiqueta.render("Nombre: ", True, (0, 0, 0))
    pantalla.blit(texto_nombre, (x + 5, y + 5))  # Texto dentro de la caja
    pantalla.blit(etiqueta, (10, 560))

    return rect_nombre


#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_reiniciar(pantalla):
    imagen_reiniciar = pygame.image.load("SUDOKU/imagenes/reiniciar.jpg")
    imagen_reinciar = pygame.transform.scale(imagen_reiniciar, (70, 70))
    
    x = 10
    y = 540
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_reinciar, (x, y))
    
    return rect_volver

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_pausa(pantalla):
    imagen_reiniciar = pygame.image.load("SUDOKU/imagenes/pausa.jpg")
    imagen_reinciar = pygame.transform.scale(imagen_reiniciar, (50, 50))
    
    x = 100
    y = 540
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_reinciar, (x, y))
    
    return rect_volver

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_reanudar(pantalla):
    imagen_reiniciar = pygame.image.load("SUDOKU/imagenes/reanudar.jpg")
    imagen_reinciar = pygame.transform.scale(imagen_reiniciar, (50, 50))
    
    x = 200
    y = 540
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_reinciar, (x, y))
    
    return rect_volver


#--------------------------------------------------------------------------------------------------------------
def dibujar_errores(pantalla):

    x = 475
    y = 30

    # Dibujar la caja de texto
    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    errores = fuente.render("Errores: ", True, (50, 90, 175))
    pantalla.blit(errores, (x + 5, y + 5))  # Texto dentro de la caja

#--------------------------------------------------------------------------------------------------------------
def dibujar_tiempo(pantalla):

    x = 150
    y = 30

    # Dibujar la caja de texto
    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    errores = fuente.render("Tiempo: ", True, (50, 90, 175))
    pantalla.blit(errores, (x + 5, y + 5))  # Texto dentro de la caja