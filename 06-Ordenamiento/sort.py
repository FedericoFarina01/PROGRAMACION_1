""" 1) Desarrollar una función que reciba una lista y ordene sus elementos utilizando un criterio pasado por parámetro, devolverá un booleano indicando si pudo ordenar los elementos o no. """
# Desarrollar una función que reciba una lista y ordene sus elementos utilizando un criterio
# pasado por parámetro, devolverá un booleano indicando si pudo ordenar los elementos o
# no.

# def ordenar_lista(lista:list, criterio:str = "asc") -> bool:
#     """
#     """
#     bandera = False
    
#     if criterio == "asc":
#         for i in range(len(lista)-1):
#             for j in range(i + 1,len(lista)):
#                 if lista[i] > lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#                     bandera = True
    
#     elif criterio == "desc":
#         for i in range(len(lista)-1):
#             for j in range(i + 1,len(lista)):
#                 if lista[i] < lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#                     bandera = True
#     return bandera


def ordenar_lista(lista:list, criterio:str = "asc") -> bool:
    """
    """
    bandera = False
    
    for i in range(len(lista)-1):
        for j in range(i + 1,len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "desc" and lista[i] < lista[j]):
                aux = lista[i] 
                lista[i] = lista[j]
                lista[j] = aux
                bandera = True
    return bandera


lista = [6, 3, 4, 1, 2, 5, -2, 9]
print(lista)    # PROHIBIDO
ordenar_lista(lista, "asc")
print(lista)    # PROHIBIDO


""" 2) Desarrollar una función que reciba 3 listas paralelas y un criterio y las ordene utilizando como base la primera lista que reciba por parámetro, devolverá un booleano indicando si pudo ordenar los elementos o no. """
nombres = ["lautaro", "tomas", "nelson", "carlos", "agustin"]
apellidos = ["veiga", "gonzales", "vega","perez", "lopez"]
edades = [20, 30 , 25 , 18 , 50]

def intercambiar_valores(lista: list, indice_a: int, indice_b: int):
    bandera = False

    if len(lista) > 1 and indice_a < len(lista) and indice_b < len(lista):
        aux = lista[indice_a]
        lista[indice_a] = lista[indice_b]
        lista[indice_b] = aux
        bandera =  True
    return bandera



def ordenar_listas_paralelas( lista_principal: list, lista_a: list, lista_b: list, criterio: str) -> bool:
    bandera = False
    for i in range(len(lista_principal) - 1):
        for j in range(i + 1, len(lista_principal)):
            if (criterio == "asc" and lista_principal[i] > lista_principal[j]) or (criterio == "desc" and lista_principal[i] < lista_principal[j]):
                intercambiar_valores(lista_principal, i, j)
                intercambiar_valores(lista_a, i, j)
                intercambiar_valores(lista_b, i, j)
                bandera = True
    
    return bandera

print(nombres)
print(apellidos) 
print(edades)             

ordenar_listas_paralelas(edades, nombres, apellidos, "desc")

print("--------------")

print(nombres)
print(apellidos) 
print(edades) 




""" 3) Desarrollar una función que reciba 2 listas paralelas y un criterio (asc desc), si los valores de la lista principal son iguales, deberá ordenar las listas utilizando la segunda lista (Ordenamiento por doble criterio). Devolverá un booleano indicando si pudo ordenar los elementos o no. """
def ordenar_listas_dobles_criterio(lista_principal:list, lista_secundaria:list, criterio:str = "asc")->bool:
    bandera = False
    for i in range(len(lista_principal) -1):
        for j in range(i + 1, len(lista_principal)):
            if (criterio == "asc" and lista_principal[i] > lista_principal[j] or (criterio == "desc" and lista_principal[i] < lista_principal[j])):
                intercambiar_valores(lista_principal, i, j)
                intercambiar_valores(lista_secundaria, i, j)
            elif lista_principal[i] == lista_principal[j] and (criterio == "asc" and lista_secundaria[i] > lista_secundaria[j] or (criterio == "desc" and lista_secundaria[i] < lista_secundaria[j])):
                intercambiar_valores(lista_secundaria, i, j)
                bandera = True
    return bandera

lista_a = [22, 54, 22, 18]
lista_b = ["damian", "cristian", "bastian", "albo"]
print(lista_a)
print(lista_b)
print("---------------------------------")
ordenar_listas_dobles_criterio(lista_a, lista_b, "desc")
print(lista_a)
print(lista_b)


""" 4) Desarrollar una función que reciba una matriz y la ordene de acuerdo al criterio recibido por parámetro. Devolverá un booleano indicando si pudo ordenar los elementos o no. 1 """