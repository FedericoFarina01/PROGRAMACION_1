import pygame
from funciones import *
from botones import *
from constantes import *
from pantallas.inicio import dibujar_pantalla_inicio, cambiar_dificultad
from pantallas.principal import dibujar_pantalla_principal
from pantallas.puntajes import dibujar_pantalla_puntajes
from pantallas.pausa import dibujar_pantalla_pausa
from pantallas.ganaste import dibujar_pantalla_ganaste

#--------------------------------------------------------------------------------------------------------------
# Inicializamos pygame
pygame.init()
#--------------------------------------------------------------------------------------------------------------

# Configuración de la pantalla
pantalla = pygame.display.set_mode(DIMENSION_PANTALLA)

#--------------------------------------------------------------------------------------------------------------

# Crear pantalla
pantalla = pygame.display.set_mode(DIMENSION_PANTALLA)

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
puntos = 1000

#--------------------------------------------------------------------------------------------------------------

# Variables para el Sudoku
celda_actual = None
sudoku_completo = None
sudoku_oculto = None
sudoku_actual = None

#--------------------------------------------------------------------------------------------------------------

# En tu ciclo principal, dentro del evento del juego, agrega la verificación:
while juego_corriendo:
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
                    # Cuando el jugador haga clic en "Jugar", generamos el Sudoku
                    tiempo_inicio = pygame.time.get_ticks()
                    pantalla_activa = "principal"
                    sudoku_completo = matriz_resolucion()
                    sudoku_oculto = matriz_oculta(sudoku_completo, dificultad)
                    sudoku_actual = sudoku_modificable(sudoku_oculto)
                    celda_actual = None
                    
                elif dibujar_boton_puntajes(pantalla).collidepoint(cursor):
                    pantalla_activa = "puntajes"

                elif dibujar_boton_salir(pantalla).collidepoint(cursor):
                    juego_corriendo = False
                    pygame.quit()
                    quit()

                elif dibujar_boton_dificultad(pantalla, dificultad).collidepoint(cursor):
                    dificultad = cambiar_dificultad(dificultad)

            # Detectar clic en los botones de la pantalla principal
            elif pantalla_activa == "principal":
                celda_actual = resaltar_celda(pantalla, celda_actual, sudoku_celdas())

                if dibujar_boton_reiniciar(pantalla).collidepoint(cursor):
                    celda_actual = None
                    sudoku_completo = matriz_resolucion()
                    sudoku_oculto = matriz_oculta(sudoku_completo, dificultad) 
                    sudoku_actual = sudoku_modificable(sudoku_oculto)

                elif dibujar_boton_volver(pantalla).collidepoint(cursor):
                    celda_actual = None
                    pantalla_activa = "inicio"

                elif dibujar_boton_pausa(pantalla).collidepoint(cursor): 
                    pantalla_activa = "pausa"

                # Verificar si el sudoku fue completado correctamente
                if ganaste_el_sudoku(sudoku_actual, sudoku_completo):
                    pantalla_activa = "ganaste"  # Si es correcto, cambiar a la pantalla de ganaste

            elif pantalla_activa == "pausa":
                if dibujar_boton_reanudar(pantalla).collidepoint(cursor): 
                        pantalla_activa = "principal"

            elif pantalla_activa == "puntajes":
                if dibujar_boton_volver(pantalla).collidepoint(cursor):
                    pantalla_activa = "inicio"

        if evento.type == pygame.KEYDOWN:
            tecla_presionada = pygame.key.name(evento.key)
            if pantalla_activa == "principal":
                sudoku_actual, celda_actual, cant_errores = ingresar_numeros(tecla_presionada, sudoku_actual, sudoku_completo, celda_actual, cant_errores)

    # Dibujar pantallas
    if pantalla_activa == "inicio":
        dibujar_pantalla_inicio(pantalla, dificultad)

    elif pantalla_activa == "puntajes":
        dibujar_pantalla_puntajes(pantalla)

    elif pantalla_activa == "principal":
        dibujar_pantalla_principal(pantalla, tiempo_inicio, cant_errores)
        rectangulo_sudoku = dibujar_matriz_sudoku(pantalla, sudoku_actual, celda_actual)
        boton_pausa = dibujar_boton_pausa(pantalla)

    elif pantalla_activa == "pausa":
        dibujar_pantalla_pausa(pantalla, ANCHO_PANTALLA, LARGO_PANTALLA)

    
    elif pantalla_activa == "ganaste":
        # Calcular tiempo transcurrido
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000  # Tiempo en segundos
        minutos = tiempo_transcurrido // 60
        segundos = tiempo_transcurrido % 60

        # Calcular puntaje
        puntaje = calcular_puntaje(cant_errores, minutos, dificultad, puntos)

        # Dibujar pantalla de ganaste con el puntaje calculado
        dibujar_pantalla_ganaste(pantalla, ANCHO_PANTALLA, LARGO_PANTALLA, puntaje)


    pygame.display.flip()