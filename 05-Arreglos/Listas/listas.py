import random

# 1) Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
def sumar_enteros(lista:list) -> int:
    """
    """
    acumulador = 0
    for numero in lista: # [4, 5, 6, 7, 8]
        acumulador += numero

    return acumulador

lista = [4, 5, 6, 7, 8]


# 2) Definir una lista que almacene los nombres de los primeros seis meses del año. Mostrar el primer y último elemento de la lista solamente.
def mostrar_meses(lista:list, indice:int) -> None:
    """
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    print(lista[indice])

# mostrar_meses(meses, 1)
# mostrar_meses(meses, -1)


# 3) Definir una lista que almacene como primer elemento el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

lista5 = ["Agustin", 10, 8]

def informar_nombre_promedio(lista:list) -> None:
    """
    Esta funcion se encarga de informar el nombre del alumno y el promedio de sus dos notas
        - Por ultimo retorna el nombre y el promedio
    """
    suma = lista[1] + lista[2]
    promedio = suma / 2
    print(f"Nombre del alumno: {lista[0]}\nPromedio: {promedio}")

# informar_nombre_promedio(lista5)

"""
4) Definir una lista con 7 elementos enteros. Contar cuántos de dichos valores almacenan un valor superior a 33.
"""
lista_numeros = [8, 7, 30, 47, 50, 2, 70]

def contar_cantidad_numeros_superiores(lista:list, valor_minimo: int)-> int:
    """
    """
    contador = 0
    for numero in lista:
        if numero > valor_minimo:
            contador += 1
    
    return contador

# print(contar_cantidad_numeros_superiores(lista_numeros, 25))

"""
5) Definir una lista con 7 elementos enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores
a 5.
"""
lista_numeros = [8, 7, 30, 47, 50, 2, 70]
def mostrar_valores_iguales_o_superiores(lista:list, valor_minimo:int)->None:
    """
    """
    for numero in lista:
        if numero >= valor_minimo:
            print(numero)

# mostrar_valores_iguales_o_superiores(lista_numeros, 5)

"""
6) Definir y cargar una lista con 10 números enteros aleatorios (utilizar random), entre 1 y 10. Contar y mostrar por
pantalla la cantidad de números pares.
"""
def generar_lista_aleatoria_numeros(cantidad_numeros:int, minimo:int, maximo:int)->list:
    """
    """
    lista_numeros = []
    for _ in range(cantidad_numeros):
        lista_numeros += [random.randint(minimo, maximo)]
    
    return lista_numeros

def contar_cantidad_numeros_pares(lista:list)->int:
    """
    """
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    
    return contador

lista_numeros_random = generar_lista_aleatoria_numeros(10, 1, 10)
print(lista_numeros_random)
print(contar_cantidad_numeros_pares(lista_numeros_random))


"""
7) Definir una lista que almacene los nombres de 4 personas. Contar cuántos de esos nombres tienen 5 o más
caracteres.
"""
def medir_coleccion(coleccion:list|str)->int:
    """
    """
    contador = 0
    for _ in coleccion:
        contador += 1
    
    return contador

def determinar_nombres_mas_de_5_caracteres(lista_nombres:list)->int:
    """
    """
    contador_palabras = 0

    for i in range(medir_coleccion(lista_nombres)):
        if medir_coleccion(lista_nombres[i]) >= 5:
            contador_palabras += 1
    
    return contador_palabras

# lista_nombres = ["Federico", "Juan", "Marcos", "Max"]
# print(determinar_nombres_mas_de_5_caracteres(lista_nombres))


"""
8) Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.
"""

def solicitar_numero(longitud_lista:int)->list:
    """
    """
    lista = []

    for i in range(longitud_lista):
        numero = int(input(f"Ingrese un número {i + 1}: "))
        lista += [numero]
    
    return lista

def imprimir_lista(lista:list)->None:
    """
    """
    for i in range(medir_coleccion(lista)):
        if i != (medir_coleccion(lista) - 1):
            print(lista[i], end= " ")
        else:
            print(lista[i])

lista_enteros = solicitar_numero(5)
imprimir_lista(lista_enteros)


"""
9) Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al
ingresar el cero. Mostrar finalmente todos los elementos cargados y el tamaño de la lista.
"""

def almacenar_datos(mensaje: str ,numero_magico: int = 0) -> list:
    lista = []
    while True:
        numero = int(input(mensaje))
        if numero == numero_magico:
            break
        else:
            lista += [numero]
    return lista

def medir_lista(lista:list) -> int:
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def mostrar_lista(lista:list) -> str:
    for elemento in lista:
        print(elemento)

lista = almacenar_datos("ingrese un numero: ") 
mostrar_lista(lista)
print("el largo de la lista es: ",medir_lista(lista))


"""
10) Almacenar en una lista los sueldos (valores float) de 7 operarios. Imprimir la lista y el promedio de sueldos
"""


def almacenar_sueldos(cantidad:int) -> list :
    lista = [None] * cantidad
    for i in range(len(lista)):
        sueldo = float(input("ingrese el sueldo del empleado: "))
        lista[i] = sueldo
    return lista

def calcular_promedio(lista:list) -> float:
    acumulador = 0
    for sueldo in lista:
        acumulador += sueldo
    promedio = acumulador / len(lista)
    return promedio

lista = almacenar_sueldos(2)
mostrar_lista(lista)
promedio = calcular_promedio(lista)
print(f"el promedio de los sueldos es: {promedio:.2f}")



# 11) Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float). Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio.

def almacenar_numeros(cantidad:int, mensaje:str) -> list :
    """
    """
    lista = [None] * cantidad # [None, None, None, None, None]
    for i in range(len(lista)):
        numero = float(input(mensaje))
        lista[i] = numero

    return lista

def calcular_promedio(lista:list) -> float:
    """
    """
    acumulador = 0
    for numero in lista:
        acumulador += numero

    promedio = acumulador / len(lista)

    return promedio

def contar_superior_promedio(promedio:float, lista:list) -> int:
    """
    """
    contador = 0
    for numero in lista:
        if numero > promedio:
            contador += 1

    return contador
    
# 12) Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.
def cargar_lista(cantidad:int, mensaje:str) -> list:
    """
    """
    lista = []

    for _ in range(cantidad):
        numero = int(input(mensaje))
        lista += [numero]

    return lista

def identificar_maximo(lista:list) -> int | None:
    """
    """
    maximo = None
    for numero in lista:
        if maximo == None or numero > maximo:
            maximo = numero

    return maximo


#13) Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y su posición.
def identificar_minimo(lista:list)-> int | None:
    minimo = None
    for numero in lista:
        if minimo == None or numero < minimo:
            minimo = numero

    return numero

def identificar_posicion(lista:list, valor_de_busqueda:int)-> int | None:
    for i in range(len(lista)):
        if lista[i] == valor_de_busqueda:
            return i 
        
""" cargar_lista(5, "Ingrese un numero: ")
minimo_identificado = identificar_minimo(lista_generada)
identificar_posicion(lista_generada, minimo_identificado)
print(f"La posicion del minimo encontrado en la lista es {posicion_identificada}") """



#14) Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de la persona con el nombre más corto.
def cargar_lista_de_strings(cantidad:int, mensaje:str)-> list:
    lista = []
    for _ in range(cantidad):
        cadena = input(mensaje)
        lista += [cadena]

    return cadena

def medir_coleccion(coleccion:list|str)->int:
    """
    """
    contador = 0
    for _ in coleccion:
        contador += 1
    
    return contador

def identificar_minimo(lista:list)-> int | None:
    minimo = None
    for numero in lista:
        if minimo == None or numero < minimo:
            minimo = numero

    return minimo



def calcular_largos(lista:list)->list:
    lista_vacia = []
    for i in range(len(lista)):
        lista_vacia += [medir_coleccion(lista[i])]

    return lista_vacia

nombres_cargados = cargar_lista_de_strings(5, "Ingrese un nombre: ") #Genero mi lista
elementos_medios = calcular_largos(nombres_cargados) #Armamos una lista de enteros que representan el largo de cada nombre
minimo = identificar_minimo #Buscamos el minimo entre los largos del nombre
indice_del_minimo = identificar_posicion(elementos_medios, minimo)
print(f"El nombre mas corto es {nombres_cargados[indice_del_minimo]}") #Imprimimos el nombre acediendo a la poscion


#15) Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
def cargar_datos_enteros(cantidad:int, mensaje:str)-> list:
    lista = []
    for _ in range(cantidad):
        numero = int(input(mensaje))
        lista += [numero]
        return lista

def identificar_maximo(lista:list)-> int | None:
    maximo = None
    for numero in lista:
        if minimo == None or numero > minimo:
            maximo = numero

    return maximo

def contar_apariciones_de_lista(lista:list, valor:int)-> int:
    contador = 0
    for elemento in lista:
        contador += 1
        return contador

lista_enteros = cargar_datos_enteros(5, "Ingrese un numero entero: ")
numero_maximo = identificar_maximo(lista_enteros)
cantidad_repeticiones = contar_apariciones_de_lista(lista_enteros, numero_maximo)
print(f"El numero maximo es: {numero_maximo} \n y se repite {cantidad_repeticiones} veces")


"""
16) Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de
realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o
iguales a 18 años). Utilizar listas paralelas.
"""

# def ingresar_nombres_edades(lista_nombres:list, lista_edades:list, cantidad:int, mensaje_nombre:str, mensaje_edad:str) -> None:
#     """

#     Función que se encarga de rellenar listas
#     """
#     for _ in range(cantidad):
#         """
#         nombre = input(mensaje_nombre)
#         edad = int(input(mensaje_edad))
#         lista_nombres += [nombre]
#         lista_edades += [edad]
#         """
#         lista_nombres += [(input(mensaje_nombre))]
#         lista_edades += [int(input(mensaje_edad))]


def ingresar_nombres_edades(cantidad:int, mensaje_nombre:str, mensaje_edad:str) -> None:
    """
    Función que se encarga de rellenar listas
    """
    lista_nombres = []
    lista_edades = []

    for _ in range(cantidad):
        """
        nombre = input(mensaje_nombre)
        edad = int(input(mensaje_edad))
        lista_nombres += [nombre]
        lista_edades += [edad]
        """
        lista_nombres += [(input(mensaje_nombre))]
        lista_edades += [int(input(mensaje_edad))]

    lista_listas = [lista_nombres, lista_edades]
    return lista_listas

def mostrar_mayores_edad(lista_nombres:list, lista_edad:list, mayor_edad:int = 18) -> None:
    """
    """
    print(f"Personas mayores a {mayor_edad}:")
    for i in range(len(lista_edad)):
        if lista_edad[i] >= mayor_edad:
            print(f"{lista_nombres[i]}")

# lista_nombres = []
# lista_edades = []

lista = ingresar_nombres_edades(5, "Ingrese su nombre: ", "Ingrese su edad: ")
lista_nombres = lista[0]
lista_edades = lista[1]
mostrar_mayores_edad(lista_nombres, lista_edades)




