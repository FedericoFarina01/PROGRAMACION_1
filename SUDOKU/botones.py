import pygame


def dibujar_boton_jugar(pantalla):
    x = 290
    y = 200
    ancho = 120
    alto = 55

    rect_jugar = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Jugar", True, (0, 0, 0))  
    texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
    if rect_jugar.collidepoint(pygame.mouse.get_pos()):
        texto_jugar = fuente.render("Jugar", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_jugar, (x + 15, y + 10))

    return rect_jugar

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_puntajes(pantalla):
    x = 290
    y = 270
    ancho = 160
    alto = 55

    rect_puntajes = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Puntajes", True, (0, 0, 0)) 
    texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
    if rect_puntajes.collidepoint(pygame.mouse.get_pos()):
        texto_puntajes = fuente.render("Puntajes", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_puntajes, (x + 15, y + 10))

    return rect_puntajes
#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_dificultad(pantalla, dificultad):
    x = 290
    y = 340
    ancho = 110
    alto = 55

    rect_dificultad = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render(dificultad, True, (0, 0, 0))
    texto_dificultad = fuente.render(dificultad, True, (0, 0, 0))
    if rect_dificultad.collidepoint(pygame.mouse.get_pos()):
        texto_dificultad = fuente.render(dificultad, True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_dificultad, (x + 15, y + 10))

    return rect_dificultad
#----------------------------------------------------------------------------------
def dibujar_boton_salir(pantalla):
    x = 290
    y = 410
    ancho = 100
    alto = 55

    rect_salir = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Salir", True, (0, 0, 0))
    texto_salir = fuente.render("Salir", True, (0, 0, 0))
    if rect_salir.collidepoint(pygame.mouse.get_pos()):
        texto_salir = fuente.render("Salir", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_salir, (x + 15, y + 10))

    return rect_salir

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_volver(pantalla):
    imagen_volver = pygame.image.load("SUDOKU/imagenes/flecha_volver.png")
    imagen_volver = pygame.transform.scale(imagen_volver, (50, 50))  

    x = 70
    y = 70
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_volver, (x, y))
    
    return rect_volver

#--------------------------------------------------------------------------------------------------------------
# EL INGRESO DEL NOMBRA VA A IR AL FINAL DE LA PARTIDA 
""" def dibujar_boton_nombre(pantalla, nombre_jugador):

    x = 200
    y = 500
    ancho = 250
    alto = 30


    rect_nombre = pygame.draw.rect(pantalla, (0, 0, 0),(x, y, ancho, alto))  # Caja nombre
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    etiqueta = fuente.render("Nombre: ", True, (0, 0, 0)) # Etiqueta
    texto_nombre = fuente.render(nombre_jugador, True, (0, 0, 0)) 
    pantalla.blit(texto_nombre, (x + 5, y + 5))  # Texto dentro de la caja
    pantalla.blit(etiqueta, (75, 510))

    return rect_nombre """


#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_reiniciar(pantalla):
    
    x = 662
    y = 290
    ancho = 120
    alto = 40
    
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_reiniciar = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20)
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_reiniciar = fuente.render("Reiniciar", True, (0, 0, 0))
    pantalla.blit(texto_reiniciar, (x + 15, y + 5))
    
    return rect_reiniciar
#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_pausa(pantalla):

    x = 12
    y = 290
    ancho = 120
    alto = 40
    
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_pausa = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_pausa = fuente.render("Pausa", True, (0, 0, 0))
    pantalla.blit(texto_pausa, (x + 28, y + 5))
    
    return rect_pausa

#--------------------------------------------------------------------------------------------------------------
def dibujar_errores(pantalla, cant_errores):
    x = 495
    y = 30

    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    errores_texto_sombra = fuente.render("Errores:", True, (0, 0, 0))
    errores_texto = fuente.render("Errores:", True, (200, 143, 90))  
    pantalla.blit(errores_texto_sombra, (x + 6 , y + 6)) 
    pantalla.blit(errores_texto, (x + 5, y + 5))
    errores_valor = fuente.render((cant_errores), True, (0, 0, 0))  
    pantalla.blit(errores_valor, (x + 90, y + 5)) 

#--------------------------------------------------------------------------------------------------------------
def dibujar_tiempo(pantalla, tiempo_inicio, x, y):

    tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000 
    minutos = tiempo_transcurrido // 60  # Minutos
    segundos = tiempo_transcurrido % 60  # Segundos restantes

    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    tiempo_texto_sombra = fuente.render("Tiempo:", True, (0, 0, 0))
    tiempo_texto = fuente.render("Tiempo:", True, (200, 143, 90))  
    pantalla.blit(tiempo_texto_sombra, (x + 1 , y + 1))  
    pantalla.blit(tiempo_texto, (x, y))  
    tiempo_valor = fuente.render(f"{minutos:02}:{segundos:02}", True, (0, 0, 0)) 
    pantalla.blit(tiempo_valor, (x + 75, y))  


