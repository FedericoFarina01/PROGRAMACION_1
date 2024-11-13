import pygame
import random
# import pygame as pg

pygame.init() # Inicializamos pygame

# Tamaños y ubicaciones: X, Y 
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

color_rectangulo = [128, 8, 108] # 
COLOR_VERDE_OSCURO = (3, 69, 20) # Color RGB Constante
# RGBA (El A es el alpha y es la transparencia del color)

pantalla = pygame.display.set_mode(dimension_pantalla) # Creacion de una pantalla con sus dimensiones
# pantalla = pygame.display.set_mode(dimension_pantalla, pygame.RESIZABLE) # Pantalla de tamaño ajustable
pygame.display.set_caption("Mi SuperJuego") # Cambia el titulo del juego

image_joystick = pygame.image.load("Programacion_I_2C/Clase_17/joystick.png") 
pygame.display.set_icon(image_joystick) # Cambio el icono de mi juego

# Imagenes:
imagen_personaje = pygame.image.load("Programacion_I_2C/Clase_17/personaje.jpg") # Cargamos una imagen a una variable
imagen_personaje = pygame.transform.scale(imagen_personaje, (225, 225)) # Ajustar el tamaño de la imagen

# Sonidos:
# De fondo (duracion larga)
pygame.mixer.init() 
pygame.mixer.music.load("Programacion_I_2C/Clase_17/test_sound.mp3")
pygame.mixer.music.set_volume(0.4) # 0 - 1

# Sonidos de efectos (duracion corta)
sonido_disparo = pygame.mixer.Sound("Programacion_I_2C/Clase_17/test_sound.mp3")
sonido_disparo.set_volume(0.1)

ubicacion_circulo_x = 700
ubicacion_circulo_y = 100

ubicacion_personaje_x = 538
ubicacion_personaje_y = 337

juego_corriendo = True

# while True # A
while juego_corriendo == True:  # B
    # for evento in pygame.event.get(): # A (Iteramos sobre todos los eventos del juego)
    lista_eventos = pygame.event.get() # B
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # Preguntamos si el usuario apreto la cruz para cerrar el juego.
            juego_corriendo = False # B
            # pygame.quit() # Cerramos el juego. # A
            # quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # print(evento) # Mostramos la ubicacion del mouse
            # ubicacion_circulo_y += 20  # Movemos el ciruculo con clicks del mouse
            # if ubicacion_circulo_y > pantalla.get_height() + 50:
            #     ubicacion_circulo_y = 100
            # ubicacion_personaje_x += 20 # Muevo la imagen del personaje

            # color_rectangulo = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] 
            # for i in range(len(color_rectangulo)): # Genero un color aleatorio para el rectangulo con cada click
            #     color_rectangulo[i] = random.randint(0, 255)

            # Transparencia de Superficies
            imagen_personaje.set_alpha(random.randint(0, 255)) # 0 -> 255

            # Sonidos:
            # pygame.mixer.music.play() # Sonido de Fondo
            sonido_disparo.play() # 

            # Comparando Rect (clase) con Superficies
            rectangulo_personaje = pantalla.get_rect()
            
    # RGB -> Red, Green, Blue. Van del 0 al 255
    pantalla.fill((118, 182, 184)) # Llena la pantalla de un color de fondo.
    # Fusiono la imagen del joystick y el personaje a la pantalla del juego.
    pantalla.blit(image_joystick, (0, 0)) 
    pantalla.blit(imagen_personaje, (ubicacion_personaje_x, ubicacion_personaje_y))

    # Dibujar figuras geometricas en la pantalla.
    # Rect (clase), consiste de Coordenada y Tamaño (X, Y, ancho, alto)
    pygame.draw.rect(pantalla, color_rectangulo, (700, 100, 100, 100)) # Dibuja un rectangulo en la pantalla.
    # Rect (clase), consiste de Coordenada (X, Y) y Radio 
    mi_circulo = pygame.draw.circle(pantalla, COLOR_VERDE_OSCURO, (ubicacion_circulo_x, ubicacion_circulo_y), 50, width=10)
    # A:     
    # pygame.display.update() # Puede recibir parametros y actualizar solamente esa parte del juego y si no recibe parametros actualiza todo.
    # B:
    pygame.display.flip() # Siempre actualiza toda la pantalla (Siempre al final del bucle)


print("Se termino el juego")