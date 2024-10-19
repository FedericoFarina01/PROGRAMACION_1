"""
1- Crear y cargar una matriz de 4x4 con datos numéricos aleatorios entre 1 y 9 inclusive, en formato string. 

"""
import random

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
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

def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    """
    """
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = str(random.randint(desde, hasta))

# Mostrar los números pares de esa matriz (en filas y columnas) y reemplazar los números impares con "#" para ocultarlos.
def ocultar_datos_matriz(matriz:list, caracter:str, valor_ocultar:int) -> None:
    """
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if int(matriz[i][j]) % 2 == valor_ocultar:
                print(caracter, end=" ")

            else:
                print(matriz[i][j], end=" ")
        
        print()

def mostrar_matriz(matriz:list) -> None:
    """
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        
        print()


"""
2- Generar una matriz de 3x3 cargando datos numéricos del 1 al 9 inclusive en celdas aleatorias, sin que se
repitan los números (al estilo Sudoku).
"""
import random

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
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

def mostrar_matriz(matriz:list) -> None:
    """
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        
        print()

matriz_sudoku = crear_matriz(3, 3, 0)

def crear_sudoku(matriz:list, minimo:int = 1, maximo:int = 9)->None:
    """
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero_random = random.randint(minimo, maximo)
            while verificar_numero_repetido(matriz, numero_random) == True:
                numero_random = random.randint(minimo, maximo)
            matriz[i][j] = numero_random

def verificar_numero_repetido(matriz:list, numero:int)->bool:
    """
    """
    bandera_numero_repetido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido



crear_sudoku(matriz_sudoku)
mostrar_matriz(matriz_sudoku)


""" 
Ejercicio 3: 
Desarrollar una función que reciba 2 matrices, los sume y devuelva la matriz resultante, sin modificar las
matrices originales.
"""
import random
def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for _ in range(cantidad_filas): 
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None: 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                print(matriz[i][j], end=" ")
        print() 


def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = random.randint(desde,hasta)


def sumar_matrices(primer_matriz:list, segunda_matriz:list) -> list | None:
    if len(primer_matriz) == len(segunda_matriz) and len(primer_matriz[0]) == len(segunda_matriz[0]):
        tercer_matriz = crear_matriz(len(primer_matriz), len(primer_matriz[0]), None)
        for i in range(len(primer_matriz)):
            for j in range(len(primer_matriz[i])):
                tercer_matriz[i][j] = primer_matriz[i][j] + segunda_matriz[i][j]
    else:
        tercer_matriz = None
    return tercer_matriz

matriz_prueba_1 = crear_matriz(3, 3, None)
matriz_prueba_2 = crear_matriz(3, 3, None)
llenar_matriz_random(matriz_prueba_1, 1, 9)
llenar_matriz_random(matriz_prueba_2, 1, 9)

mostrar_matriz(matriz_prueba_1)
print("---------------------------------------------")
mostrar_matriz(matriz_prueba_2)
print("---------------------------------------------")
matrices_sumadas = sumar_matrices(matriz_prueba_1, matriz_prueba_2)
mostrar_matriz(matrices_sumadas)



# 4- Desarrollar una función que reciba una matriz y un número escalar, multiplicar la matriz por el número
# escalar y retornar la matriz resultante, sin modificar la matriz original.

import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:any)->list:
    matriz = []

    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz

def llenar_matriz_aleatoriamente(matriz_vacia:list, desde:int, hasta:int)->None:
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = str(random.randint(desde,hasta))

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def multiplicar_matriz_por_escalar(matriz: list, escalar: int)->list:
    """
    """
    matriz_resultante = []
    fila = []
    for i in range(len(matriz)): #Recorre las filas de la matriz
        for j in range (len(matriz[i])): #Recorre las columnas de cada fila
            fila += [int(matriz[i][j]) * escalar] #Agrega un dato a la fila por cada iteración
        matriz_resultante += [fila] #Se agrega esa fila a la matriz
        fila = []
    
    return matriz_resultante

# matriz_prueba = inicializar_matriz(4, 5, None)
# llenar_matriz_aleatoriamente(matriz_prueba, 1, 9)
# matriz_resultante = multiplicar_matriz_por_escalar(matriz_prueba, 2)
# mostrar_matriz(matriz_prueba)
# print("------------------------")
# mostrar_matriz(matriz_resultante)



import random

# 5- Desarrollar una función que reciba dos matrices, y las multiplique entre sí. Se debe validar que las matrices
# recibidas por parámetro se puedan multiplicar entre sí y devolver la matriz resultante, sin alterar las matrices
# originales, caso contrario la función devolverá un None.


def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for _ in range(cantidad_filas): 
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None: 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                print(matriz[i][j], end=" ")
        print() 


def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = random.randint(desde,hasta)

# 
# 1 2 3 |  1 2       = 22  28 
# 4 5 6 |  3 4       = 49  64
#          5 6


# 2 * 3 | 3 * 2 = multiplicacion de las filas de la primer matriz por las columnas de la segunda matriz

def multiplicar_matrices(matriz_a:list ,matriz_b:list) -> list | None:
    matriz_resultante = None
    if len(matriz_a[0]) == len(matriz_b):
        matriz_resultante = crear_matriz(len(matriz_a), len(matriz_b[0]), 0)
        for i in range(len(matriz_a)): #2 iteraciones
            for j in range(len(matriz_b[0])): #2 iteraciones
                for k in range(len(matriz_b)): #3 iteraciones por cada iteracion de las anteriores
                    matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_resultante

matriz = crear_matriz(2, 3, None)
matriz_2 = crear_matriz(3, 2, None)
resultado = llenar_matriz_random(matriz,1, 6)
resultado = llenar_matriz_random(matriz_2,1, 6)

mostrar_matriz1 = mostrar_matriz(matriz) 
print("------------------------------------")
mostrar_matriz2 = mostrar_matriz(matriz_2)
print("------------------------------------")

resultado1 = multiplicar_matrices(matriz, matriz_2)
mostrar_matriz(resultado1)


