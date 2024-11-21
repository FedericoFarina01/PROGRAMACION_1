import pygame
# import random

pygame.init()


pantalla = pygame.display.set_mode((800, 600))
imagen_personaje = pygame.image.load("Programacion_I_2C/Clase_17/personaje.jpg")
imagen_roca = pygame.image.load("Programacion_I_2C/Clase_17/roca.jpg")
imagen_personaje_rect = imagen_personaje.get_rect() # Rect -> Ubicacion y Tamaño (COLISIONES)
imagen_personaje_rect.y = 525
imagen_personaje_rect.x = 400
imagen_roca_rect = imagen_roca.get_rect()
imagen_roca_rect.x = 550
imagen_roca_rect.y = 350


# Timers y Eventos propios:
mi_evento_segundo = pygame.USEREVENT + 1
un_segundo = 1000 # 1000 milisegundos = 1 segundo 
tick_personaje = 15
evento_movimiento_personaje = pygame.USEREVENT + 2
pygame.time.set_timer(mi_evento_segundo, un_segundo)
pygame.time.set_timer(evento_movimiento_personaje, tick_personaje)
contador = 0



# Texto
# texto_string = "Hola " # O vacio y se va modificando al apretarse una key unicode.
fuente = pygame.font.SysFont("Arial", 72, bold=True)
texto = fuente.render("", True, "yellow") # Colores, en ingles en letra (str), o valores RGB
texto_rect = texto.get_rect()
ingreso = ""

#reloj = pygame.time.Clock()

corriendo = True
while corriendo == True:
    #reloj.tick(60)
    #print(pygame.time.get_ticks())
    #print(reloj.get_fps())

    # Teclado Version 2
    lista_teclas_apretadas = pygame.key.get_pressed()
    #print(lista_teclas_apretadas)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE: # Borrar
                ingreso = ingreso[0:-1] # Borro el ultimo caracter
            elif evento.key == pygame.K_RETURN:  # Enter
                print("DEJO DE ESCRIBIR")
            else:
                ingreso += evento.unicode # Escribo cualquiera de los caracteres excepto los de if y elif.
        # if evento.type == mi_evento_segundo:
        #     contador += 1
        #     texto = fuente.render(ingreso, True, "yellow")
        #     if imagen_personaje_rect.colliderect(imagen_roca_rect) == True:
        #         print(f"Colisionooooo {contador}")
            #print(f"Pasaron {contador} segundos.")
        if evento.type == evento_movimiento_personaje:
            if lista_teclas_apretadas[pygame.K_LEFT] == True:
                imagen_personaje_rect.x -= 1
                if imagen_personaje_rect.colliderect(imagen_roca_rect) == True: # Colision roca con personaje.
                    imagen_personaje_rect.x += 1
            if lista_teclas_apretadas[pygame.K_RIGHT] == True:
                imagen_personaje_rect.x += 1
                if imagen_personaje_rect.colliderect(imagen_roca_rect) == True:
                    imagen_personaje_rect.x -= 1
            if lista_teclas_apretadas[pygame.K_UP] == True:
                imagen_personaje_rect.y -= 1
                if imagen_personaje_rect.colliderect(imagen_roca_rect) == True:
                    imagen_personaje_rect.y += 1
            if lista_teclas_apretadas[pygame.K_DOWN] == True:
                imagen_personaje_rect.y += 1
                if imagen_personaje_rect.colliderect(imagen_roca_rect) == True:
                    imagen_personaje_rect.y -= 1

        if evento.type == pygame.MOUSEBUTTONDOWN: # Colision contra el click del mouse.
            if imagen_personaje_rect.collidepoint(pygame.mouse.get_pos()) == True:
                print("Clickeaste el personaje")
            #mouse = pygame.mouse.get_pos()
            # imagen_personaje.set_alpha(random.randint(0, 255)) # Transparencia de alguna superficie.
            # print(mouse)
            # if mouse[0] >= imagen_personaje_rect.x and mouse[0] <= imagen_personaje_rect.x + imagen_personaje_rect.width and mouse[1] >= imagen_personaje_rect.y and mouse[1] <= imagen_personaje_rect.y + imagen_personaje_rect.height:
            #     print("Clickeaste el personaje")

        # Teclado
        # if evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_LEFT:
        #         imagen_personaje_rect.x -= 20
        #     if evento.key == pygame.K_RIGHT:
        #         imagen_personaje_rect.x += 20
        #     if evento.key == pygame.K_UP:
        #         imagen_personaje_rect.y -= 20
        #     if evento.key == pygame.K_DOWN:  
        #         imagen_personaje_rect.y += 20

        # Mouse
        # if evento.type == pygame.MOUSEBUTTONDOWN:   # Reconocer los 5 botones del mouse/ruedita
        #     print(evento.button)
        # if evento.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pressed())[0] == True: # Version 2 (sin ruedita)
        #     print("APRETE EL BOTON -> Mouse Down")
        # if evento.type == pygame.MOUSEBUTTONUP:
        #     print("DEJE DE APRETAR EL BOTON -> Mouse Up")
        # if evento.type == pygame.MOUSEMOTION:
        #     print(f"MOVI EL MOUSE {pygame.mouse.get_pos()}")
        # if evento.type == pygame.MOUSEWHEEL:
        #     print("Active ruiedita del mouse")
    #print(pygame.mouse.get_pressed())

    # if imagen_personaje_rect.colliderect(imagen_roca_rect) == True:
    #     print("Colisionooooo")
    
    # if imagen_personaje_rect.collidepoint(pygame.mouse.get_pos()) == True: # Reacciona al poner el cursor SOBRE la imagen/rectangulo.
    #     print("Clickeaste el personaje")

    pantalla.fill((0, 0, 0))
    texto = fuente.render(ingreso, True, "yellow")
    pygame.draw.rect(pantalla, (128, 128, 128), (90, 90, 250, 100), width=10, border_radius=15)
    pantalla.blit(imagen_personaje, imagen_personaje_rect)
    pantalla.blit(imagen_roca, imagen_roca_rect)
    pantalla.blit(texto, (100, 100))
    # Transicion -> Empieza con transparencia 0, va inrementandose con timer/evento, llega a 255, cambian la pantalla. Bajan la transparencia desde 255 hasta llegar a 0.
    pygame.display.flip()

pygame.quit()