import pygame
from funciones import *
from botones import *
from pantallas.inicio import dibujar_pantalla_inicio, cambiar_dificultad
from pantallas.principal import dibujar_pantalla_principal
from pantallas.puntajes import dibujar_pantalla_puntajes
from pantallas.pausa import dibujar_pantalla_pausa


#--------------------------------------------------------------------------------------------------------------

# Inicializamos pygame
pygame.init()

#--------------------------------------------------------------------------------------------------------------

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

#--------------------------------------------------------------------------------------------------------------

# Crear pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

#--------------------------------------------------------------------------------------------------------------

# Cambiar el título del juego
pygame.display.set_caption("Sudoku")

#--------------------------------------------------------------------------------------------------------------

# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono)

#--------------------------------------------------------------------------------------------------------------

# Música
""" pygame.mixer.init()
pygame.mixer.music.load("SUDOKU/musica/Vibe Mountain.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1) """

#--------------------------------------------------------------------------------------------------------------

# Variables
juego_corriendo = True
pantalla_activa = "inicio"
nombre_jugador = ""
click_izq = pygame.MOUSEBUTTONDOWN
dificultad = "Facil"
cant_errores = 0

#--------------------------------------------------------------------------------------------------------------

# Generar el Sudoku inicial
sudoku_completo = matriz_resolucion()
sudoku_actual = generar_sudoku(dificultad)
celda_actual = None

#--------------------------------------------------------------------------------------------------------------

while juego_corriendo:
    # Iterar sobre todos los eventos
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            juego_corriendo = False
            pygame.quit()
            quit()

        # Detectar clics del mouse
        if evento.type == click_izq:
            cursor = pygame.mouse.get_pos()

            # Detectar clic en los botones de la pantalla de inicio
            if pantalla_activa == "inicio":
                if dibujar_boton_jugar(pantalla).collidepoint(cursor):
                    #fade_out(pantalla)
                    tiempo_inicio = pygame.time.get_ticks()
                    sudoku_actual = generar_sudoku(dificultad)  # Generar Sudoku al iniciar el juego
                    pantalla_activa = "principal"
                    #fade_in(pantalla)

                elif dibujar_boton_puntajes(pantalla).collidepoint(cursor):
                    #fade_out(pantalla)
                    pantalla_activa = "puntajes"
                    #fade_in(pantalla)

                elif dibujar_boton_salir(pantalla).collidepoint(cursor):
                    juego_corriendo = False
                    pygame.quit()
                    quit()

                # Detectar clic en el botón de "Dificultad"
                elif dibujar_boton_dificultad(pantalla, dificultad).collidepoint(cursor):
                    dificultad = cambiar_dificultad(dificultad)

            # Detectar clic en el botón "Volver" en las pantallas "principal" y "puntajes"
            elif pantalla_activa == "principal":
                celda_actual = resaltar_celda(pantalla, celda_actual, sudoku_celdas())
                print(celda_actual)

                if dibujar_boton_reiniciar(pantalla).collidepoint(cursor):
                    celda_actual = None
                    sudoku_actual = generar_sudoku(dificultad) # Generar un Sudoku nuevo
                    cant_errores = 0
                    tiempo_inicio = pygame.time.get_ticks() # Reiniciar el temporizador

                elif dibujar_boton_volver(pantalla).collidepoint(cursor):
                    #fade_out(pantalla)
                    celda_actual = None
                    pantalla_activa = "inicio"
                    #fade_in(pantalla)
                    #pygame.mixer.music.play(-1)

                elif dibujar_boton_pausa(pantalla).collidepoint(cursor): 
                    pantalla_activa = "pausa" 

            elif pantalla_activa == "pausa":
                if dibujar_boton_reanudar(pantalla).collidepoint(cursor): 
                        pantalla_activa = "principal"


            elif pantalla_activa == "puntajes":
                if dibujar_boton_volver(pantalla).collidepoint(cursor):
                    #fade_out(pantalla)
                    pantalla_activa = "inicio"

                    #fade_in(pantalla)

#--------------------------------------------------------------------------------------------------------------

        if evento.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(evento.key)
                ingresar_numeros(tecla_presionada, sudoku_actual, sudoku_completo, celda_actual, cant_errores)


#--------------------------------------------------------------------------------------------------------------

    # Dibujar pantallas
    if pantalla_activa == "inicio":
        dibujar_pantalla_inicio(pantalla, dificultad)

    elif pantalla_activa == "puntajes":
        dibujar_pantalla_puntajes(pantalla)

    elif pantalla_activa == "principal":
        dibujar_pantalla_principal(pantalla, tiempo_inicio, cant_errores)
        rectangulo_sudoku = dibujar_matriz_sudoku(pantalla, sudoku_actual, celda_actual)
        boton_pausa = dibujar_boton_pausa(pantalla)  # Línea nueva: Dibuja el botón de pausa

    # Nueva sección: Pantalla de pausa
    elif pantalla_activa == "pausa":
        dibujar_pantalla_pausa(pantalla, ancho_pantalla, largo_pantalla)


    pygame.display.flip()  # Actualiza la pantalla