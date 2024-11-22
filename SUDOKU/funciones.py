import random

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

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:int) -> list:
    """
    Esta función se encarga de crear una matriz vacía
        Recibe:
            cantidad_filas (int): representa las filas que va a tener la matriz
            cantidad_columans (int): representa las columnas que va a tener la matriz

        Devuelve:
            matriz (list): la matriz creada a través de los parámetros
    """
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
    for i in range(len(matriz)):
        if matriz[i][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_submatriz(matriz: list, fila: int, columna: int, numero: int) -> bool:
    """
    Verifica si un número está repetido en la submatriz 3x3 correspondiente al lugar de la celda indicada.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        fila (int): Índice de la fila de la celda a verificar.
        columna (int): Índice de la columna de la celda a verificar.
        numero (int): Número que se desea verificar.
    
    Retorna:
        bool: True si el número ya está presente en la submatriz 3x3 correspondiente a la celda, 
                False en caso contrario.
    """
    # Determinar inicio_fila basado en los indices de la fila.
    if fila < 3:
        inicio_fila = 0
    elif fila < 6:
        inicio_fila = 3
    else:
        inicio_fila = 6
    #------------------------------------------
    # Determinar inicio_columna basado en los indices de la columna.
    if columna < 3:
        inicio_columna = 0
    elif columna < 6:
        inicio_columna = 3
    else:
        inicio_columna = 6
    #------------------------------------------
    resultado = False
    for fila in range(inicio_fila, inicio_fila + 3):
        for columna in range(inicio_columna, inicio_columna + 3):
            if matriz[fila][columna] == numero:
                resultado = True  # Se repiten los numeros
                break  
        if resultado:
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def generar_tablero_sudoku(valor_filas: int = 9, valor_columnas: int = 9, valor_inicial: int = 0, desde: int = 0, hasta: int = 8) -> list:
    """
    Genera una matriz 9x9 que sigue las reglas del Sudoku.
    
    Retorna:
        list: Matriz 9x9 con un Sudoku válido.
    """
    matriz = crear_matriz(valor_filas, valor_columnas, valor_inicial)  # Crear matriz vacía 9x9 con ceros
    
    for fila in range(desde, hasta + 1):
        for columna in range(desde, hasta + 1):
            numeros_disponibles = list(range(1, 10))
            random.shuffle(numeros_disponibles)  # Mezclar números posibles para colocar
            
            for numero in numeros_disponibles:
                if (not verificar_numero_repetido_en_fila(matriz, numero, fila) and
                    not verificar_numero_repetido_en_columna(matriz, numero, columna) and
                    not verificar_numero_repetido_en_submatriz(matriz, fila, columna, numero)):
                    matriz[fila][columna] = numero
                    break
            # Si no es posible colocar un número válido, reiniciamos el proceso
            if matriz[fila][columna] == 0:
                return generar_tablero_sudoku(valor_filas, valor_columnas, valor_inicial, desde, hasta)  # Llamada recursiva sin pasar la matriz
    return matriz

# Ejemplo de uso:
matriz_sudoku = generar_tablero_sudoku()
mostrar_matriz_sudoku(matriz_sudoku)
print("\nMatriz Sudoku generada correctamente!")
