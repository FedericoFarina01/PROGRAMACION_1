import pygame
import random
#----------------------------------------------------------------------------------------------------------------------------------

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

    # Determinar inicio_columna basado en los indices de la columna.
    if columna < 3:
        inicio_columna = 0
    elif columna < 6:
        inicio_columna = 3
    else:
        inicio_columna = 6

    resultado = False
    # Recorrer las submatrices 3x3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if matriz[i][j] == numero:
                resultado = True  # Se repiten los numeros
                break  # Salir del ciclo si encontramos el número
        if resultado:  # Si ya encontramos el número, salimos del ciclo exterior
            break
    return resultado

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
    if fila < 0 or fila >= len(matriz):
        print("Indice de fila fuera de rango")
    
    resultado = False
    for j in range(len(matriz[fila])):
        if matriz[fila][j] == numero:
            resultado = True  # Número repetido en la fila
            break  # Salir del ciclo si encontramos el número
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
    if columna < 0 or columna >= len(matriz[0]):
        print("Índice de columna fuera de rango")
    
    resultado = False
    for i in range(len(matriz)):
        if matriz[i][columna] == numero:
            resultado = True  # Número repetido en la columna
            break  # Salir del ciclo si encontramos el número
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def logica_sudoku(matriz: list) -> bool:
    """
    Genera un tablero de Sudoku válido utilizando la lógica del Sudoku de manera determinista.
    """
    tablero_completo = True  # Asumimos inicialmente que el tablero está completo

    # Buscar la primera celda vacía (valor 0).
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == 0:  # Si la celda está vacía
                tablero_completo = False  # El tablero no está completo aún

                # Probar con los números del 1 al 9 de manera aleatoria
                for numero in random.sample(range(1, 10), 9):
                    # Verificar si el número no está repetido en la fila, columna o submatriz
                    if (not verificar_numero_repetido_en_fila(matriz, numero, fila) and
                        not verificar_numero_repetido_en_columna(matriz, numero, columna) and
                        not verificar_numero_repetido_en_submatriz(matriz, fila, columna, numero)):
                        
                        matriz[fila][columna] = numero  # Colocar el número en la celda

                        # Llamar recursivamente para llenar el resto de las celdas
                        if logica_sudoku(matriz):  # Intentar resolver el resto del tablero
                            return True  # Si la lógica del Sudoku fue exitosa, retornar True
                        
                        # Retroceder si no fue posible
                        matriz[fila][columna] = 0  # Borrar el número si no fue válido
                # Si no se pudo colocar ningún número válido, no hay solución posible para esta celda
                return False  # No continuar con la recursión si no hay soluciones válidas para esta celda
    # Si no se encontró ninguna celda vacía, el Sudoku ha sido completado
    return tablero_completo  # Retorna True si todas las celdas están llenas


# ESTA ULTIMA FUNCION ES LA QUE HAY QUE REVISAR QUE ES LA LOGICA DEL JUEGO.




# Ejemplo de uso
matriz_sudoku = crear_matriz(9, 9, 0)  # Crear una matriz 9x9 vacía
exito = logica_sudoku(matriz_sudoku)
mostrar_matriz_sudoku(matriz_sudoku)


#---------------------------------------------------------------------------------



