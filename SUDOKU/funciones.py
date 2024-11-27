import random
import pygame

def mostrar_matriz_sudoku(matriz: list) -> None:
    """
    Muestra la matriz de Sudoku con separaciones de submatrices cada 3 filas y columnas.

    Parámetros:
        matriz (list): Matriz del Sudoku que se desea mostrar.

    Retorna:
        None: Esta función no retorna ningún valor.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:  # Separación horizontal cada 3 filas
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:  # Separación vertical cada 3 columnas
                print("|", end=" ")
            print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def inicializar_tablero_9x9(cantidad_filas: int = 9, cantidad_columnas: int = 9, valor_inicial: int = 0) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_fila(matriz: list, numero: int, fila: int) -> bool:
    """
    Verifica si un número está repetido en la fila especificada de la matriz de Sudoku.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        numero (int): El número que se desea verificar.
        fila (int): Índice de la fila donde se desea verificar.
    
    Retorna:
        bool: True si el número está repetido en la fila, False en caso contrario.
    """
    
    resultado = False
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_columna(matriz: list, numero: int, columna: int) -> bool:
    """
    Verifica si un número está repetido en la columna especificada de la matriz de Sudoku.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        numero (int): El número que se desea verificar.
        columna (int): Índice de la columna donde se desea verificar.
    
    Retorna:
        bool: True si el número está repetido en la columna, False en caso contrario.
    """
    
    resultado = False
    for fila in range(len(matriz)):
        if matriz[fila][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------
def obtener_posicion_inicial_de_fila(fila:int) -> int:
    posicion_de_fila = 0
    if fila < 3:
        posicion_de_fila = 0
    elif fila < 6:
        posicion_de_fila = 3
    else:
        posicion_de_fila = 6
    return posicion_de_fila

#---------------------------------------------------------------------------------------------------------------------------------
def obtener_posicion_inicial_de_columna(columna:int) -> int:
    posicion_de_columna = 0
    if columna < 3:
        posicion_de_columna = 0
    elif columna < 6:
        posicion_de_columna = 3
    else:
        posicion_de_columna = 6
    return posicion_de_columna

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_submatriz(matriz:list, numero:int, posicion_inicial_en_fila:int, posicion_inicial_en_columna:int) -> bool:
    bandera_numero_repetido = False
    for indices_fila in range(posicion_inicial_en_fila, posicion_inicial_en_fila + 3):
        for indices_columna in range(posicion_inicial_en_columna, posicion_inicial_en_columna + 3):
            if matriz[indices_fila][indices_columna] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido

#---------------------------------------------------------------------------------------------------------------------------------

def lista_posibles_numeros(desde: int = 1, hasta: int = 9) -> list:
    posibles_numeros = list(range(desde, hasta + 1))
    return posibles_numeros

#---------------------------------------------------------------------------------------------------------------------------------

def es_numero_valido(matriz: list, numero: int, fila: int, columna: int) -> bool:
    numero_valido = False
    if (not verificar_numero_repetido_en_fila(matriz, numero, fila) and
        not verificar_numero_repetido_en_columna(matriz, numero, columna) and
        not verificar_numero_repetido_en_submatriz(matriz, numero, obtener_posicion_inicial_de_fila(fila), obtener_posicion_inicial_de_columna(columna))):
        matriz[fila][columna] = numero
        numero_valido = True
    return numero_valido

#---------------------------------------------------------------------------------------------------------------------------------

def resolver_sudoku(matriz: list, posibles_numeros: list) -> bool:
    solucion_encontrada = True
    for fila in range(9):
        for columna in range(9):
            if matriz[fila][columna] == 0:
                solucion_encontrada = False 
                random.shuffle(posibles_numeros)
                for numero in posibles_numeros:
                    if es_numero_valido(matriz, numero, fila, columna):
                        matriz[fila][columna] = numero
                        if resolver_sudoku(matriz, posibles_numeros):
                            solucion_encontrada = True
                            break
                        matriz[fila][columna] = 0
                break
        if solucion_encontrada == False:
            break
    return solucion_encontrada

#---------------------------------------------------------------------------------------------------------------------------------

tablero = inicializar_tablero_9x9()
posibles_numeros = lista_posibles_numeros()
resolver_sudoku(tablero, posibles_numeros)
mostrar_matriz_sudoku(tablero)
print("\n")

#---------------------------------------------------------------------------------------------------------------------------------

def mostrar_tablero_oculto(matriz: list, celdas_ocultas: list, caracter: str) -> None:
    """
    Muestra el tablero de Sudoku con ciertas celdas ocultas.
    
    Parámetros:
        matriz (list): Matriz de Sudoku.
        celdas_ocultas (list): Lista de posiciones (fila, columna) de las celdas ocultas.
        caracter (str): Carácter que se mostrará en las celdas ocultas.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")

            if (fila, columna) in celdas_ocultas:
                print(caracter, end=" ")
            else:
                print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def generar_celdas(tamaño_del_tablero: int = 9) -> list:
    """
    Genera una lista de todas las posiciones del tablero.
    
    Args:
        tamaño_del_tablero (int): Tamaño del tablero (n x n).
        
    Returns:
        list: Lista de tuplas con las posiciones del tablero.
    """
    celdas = []
    for fila in range(tamaño_del_tablero):
        for columna in range(tamaño_del_tablero):
            celdas.append((fila, columna))
    return celdas

#---------------------------------------------------------------------------------------------------------------------------------

def seleccionar_celdas_ocultas(celdas, celdas_a_ocultar):
    """
    Selecciona aleatoriamente las celdas que se van a ocultar.
    
    Args:
        celdas (list): Lista de celdas disponibles.
        celdas_a_ocultar (int): Número de celdas a ocultar.
        
    Returns:
        list: Lista de celdas seleccionadas para ocultar.
    """
    celdas_a_ocultar = random.sample(celdas, celdas_a_ocultar)
    return celdas_a_ocultar

#---------------------------------------------------------------------------------------------------------------------------------

def ocultar_datos_matriz_segun_dificultad(matriz: list, dificultad: str) -> list:
    """
    Función para ocultar celdas aleatorias en el tablero según el nivel de dificultad.
    
    Args:
        matriz (list): Matriz del Sudoku (9x9) que se desea modificar.
        
    Returns:
        list: Matriz modificada con celdas ocultas.
    """
    total_celdas = 81
    celdas_a_ocultar = 0
    # Determinamos cuántas celdas ocultar según la dificultad
    if dificultad == "Facil":
        celdas_a_ocultar = int(total_celdas * 0.20)  # 20% de las celdas = 16
    elif dificultad == "Medio":
        celdas_a_ocultar = int(total_celdas * 0.40)  # 40% de las celdas = 34
    elif dificultad == "Dificil":
        celdas_a_ocultar = int(total_celdas * 0.60)  # 60% de las celdas = 48

    # Generar todas las celdas del tablero
    celdas = generar_celdas()

    # Seleccionar aleatoriamente las celdas que se van a ocultar
    celdas_ocultas = seleccionar_celdas_ocultas(celdas, celdas_a_ocultar)

    # Ocultar las celdas en la matriz
    for fila, columna in celdas_ocultas:
        matriz[fila][columna] = " "  # Valor de celda oculta
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------
def dibujar_matriz_sudoku(pantalla, matriz, celda_actual):
    """
    Dibuja la matriz de Sudoku en la pantalla de Pygame.

    Parámetros:
        pantalla: La pantalla de Pygame donde se dibujará.
        matriz: La matriz de Sudoku que se debe mostrar.
    """
    # Colores
    color_linea = (0, 0, 0)
    color_numeros= (0, 0, 0)  # Negro para los números
    color_celda_actual = (255, 255, 255)

    # Coordenadas de inicio y tamaño de celdas
    inicio_x = 150
    inicio_y = 60
    tamaño_celda = 55 # Cada celda será de 50x50 píxeles

    rect_tablero = pygame.Rect(inicio_x, inicio_y, 9 * tamaño_celda, 9 * tamaño_celda)

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
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            numeros = fuente.render(str(matriz[fila][columna]), True, color_numeros)
            x = inicio_x + columna * tamaño_celda + tamaño_celda // 3
            y = inicio_y + fila * tamaño_celda + tamaño_celda // 4

            # Si la celda es la seleccionada, la resaltamos en blanco
            if celda_actual == (fila, columna):
                pygame.draw.rect(pantalla, color_celda_actual, 
                                 (inicio_x + columna * tamaño_celda, inicio_y + fila * tamaño_celda, tamaño_celda, tamaño_celda))
            pantalla.blit(numeros, (x, y))

    return rect_tablero
#------------------------------------------------------------------------------------------
def resaltar_celda(pantalla, celda_actual,sudoku_actual):
    """
    Dibuja el Sudoku y resalta la celda clickeada en blanco.
    """
    inicio_x = 150 
    inicio_y = 60  
    tamaño_celda = 55 

    rect_tablero = pygame.Rect(inicio_x, inicio_y, 9 * tamaño_celda, 9 * tamaño_celda)

    # Recorrer celdas
    for fila in range(9):
        for columna in range(9):
            # Calcular la superficie de la celda
            rect_celda = pygame.Rect(inicio_x + columna * tamaño_celda, inicio_y + fila * tamaño_celda, tamaño_celda, tamaño_celda)

            # Detectar si el mouse está dentro de la celda
           
            if rect_celda.collidepoint(pygame.mouse.get_pos()):
                celda_actual = (fila, columna)  
                pygame.draw.rect(pantalla, (255, 255, 255), rect_celda)  # Resaltar la celda
            elif not rect_tablero.collidepoint(pygame.mouse.get_pos()):
                celda_actual = None

    if celda_actual != None and sudoku_actual[celda_actual[0]][celda_actual[1]] != ' ':
        celda_actual = None
        

    return celda_actual 

#--------------------------------------------------------------------------------------------

def generar_sudoku(dificultad):
    sudoku = inicializar_tablero_9x9(9, 9, 0)
    resolver_sudoku(sudoku, lista_posibles_numeros())
    ocultar_datos_matriz_segun_dificultad(sudoku, dificultad)
    return sudoku
#--------------------------------------------------------------------------------------------