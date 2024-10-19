# # mi_matriz = [[1, 2, 3, 4], 
# #             [10, 20, 30, 40]]

# #print(mi_matriz)



def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print("")

#mostrar_matriz(mi_matriz)

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial)->list:
    matriz=[]
    for _ in range(cant_filas):
        fila =[valor_inicial] * cant_columnas
        matriz +=[fila]
    return matriz

mi_matriz = inicializar_matriz(3,4,0)

mostrar_matriz(mi_matriz)

def cargar_matriz_secuencialmente(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]= int(input(f"Fila {i} columna {j}:"))


#cargar_matriz_secuencialmente(mi_matriz)

#mostrar_matriz(mi_matriz)

def cargar_matriz_aleatoriamente(matriz:list):
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de la fila: "))
        columna = int(input("Indice de la columna: "))
        dato =int(input("Ingrese el elemento a cargar: "))
        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando elementos? S/N: ")

#cargar_matriz_aleatoriamente(mi_matriz)

#mostrar_matriz(mi_matriz)



otra_matriz=[["a","b","c"],["x","y","z"]]


def buscar_coordenadas(matriz:list, valor):
    lista_coordenadas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                lista_coordenadas = [i,j]
                #print(f"Se encontró el valor en la fila: {i} - columna {j}")
    return lista_coordenadas

print(buscar_coordenadas(otra_matriz, "k"))



# mostrar_matriz(otra_matriz)

# print(otra_matriz[1][1])

# otra_matriz[1][1] = "?"

# mostrar_matriz(otra_matriz)


