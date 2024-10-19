import random

# PUNTO A) 
def solicitar_numero_entero(mensaje:str, mensaje_error:str,  minimo:int, maximo:int) -> int:
    """
    Esta función verifica si una cadema ingresada por el usuario es un numero entero dentro de un rango entre otros dos números enteros.
        
        Recibe:
            mensaje (str): representa el mensaje a mostrar para el usuario al ingresar el número
            minimo (int): representa el mínimo del rango en el cual se analiza el número
            maximo (int): representa el maximo del rango en el cual se analiza el número
        
        Retorna:
            numero (int): representa ingresado ya validado
    """

    bandera = False

    while bandera == False:
        numero = input(mensaje)
        if len(numero) > 0: # Verifico que sea > 0 porque sino me tiraba error al pulsa ENTER sin ingresar nada
            bandera = verificar_int(numero) # Verifica si todos los caracteres son enteros

    numero = int(numero) 

    while validar_numero_entero_en_rango(numero, minimo, maximo) != True: # Verificamos el rango
        bandera = False

        while bandera == False:
            numero = input(mensaje_error) # Si el número no se encuentra entre 3 y 15, lanza un mensaje de error.
            bandera = verificar_int(numero) 

        numero = int(numero) 

    return numero
    
#----------------------------------------
def verificar_int(string:str) -> bool:
    """
    Esta funcion verifica si todos los digitos de una cadena son numeros enteros
        
        Recibe:
            cadena (str): Representa la cadena a verificar.
        
        Retorna:
            retorno (bool):
                True: Si toda la cadena son digitos del 0 al 9
                False: Si la cadena tiene un caracter que no sea numerico.
    """

    retorno = True
    for digito in string:
        if ord(digito) < 48 or ord(digito) > 57: # Rango de las mayúsulas en código ASCII
            retorno = False
            break

    return retorno

#----------------------------------------
def validar_numero_entero_en_rango(numero:int, minimo:int, maximo:int) -> bool|None:
    """
    La función determina si un número se encuentra dentro de un rango determinado por dos enteros.
        
        Recibe:
            numero (int): representa el número a analizar
            minimo (int): representa el mínimo del rango en el cual se analiza el número
            maximo (int): representa el máximo del rango en el cual se analiza el número
        
        Retorna:
            retorno (bool|None): retorna True si el número se encuentra dentro del rango, False si no se encuentra dentro del rango y None si alguno de los parámetros no es entero (int)
    """

    retorno = None
    
    if type(numero) == int and type(minimo) == int and type(maximo) == int: # Validación de tipos
        if numero >= minimo and numero <= maximo: 
            retorno = True
        else:
            retorno = False

    return retorno

#--------------------------------------------------------------------------------

# PUNTO B) 
def generar_lista_aleatoria_mayusculas(cantidad_letras:int)->list:
    """
    Esta función genera una lista de letras mayusculas aleatorias de longitud *cantidad_letras
        
        Recibe:
           cantidad_letras (int): representa la longitud de la lista
        
        Retorna:
            lista_mayusculas (list): representa la lista generada
    """

    lista_mayusculas = []
    minimo = ord("A")
    maximo = ord("Z")
    for _ in range(cantidad_letras):
        lista_mayusculas += chr(random.randint(minimo, maximo)) # Genera un numero aleatorio entre el rango ASCII de las mayúsculas y lo convierte a su equivalente en letra
    return lista_mayusculas

#---------------------------------------------------------------------------------

# PUNTO C)
def mostrar_lista(lista: list):
    """
    Esta función muestra por consola la lista pasada por parámetro.
        
    Recibe:
       lista (list): representa la lista a mostrar.        
    """

    for i in range(len(lista)):
        if i != len(lista) - 1:
            print(lista[i], end=" - ")
        else:
            print(lista[i])
        
#---------------------------------------------------------------------------------

# PUNTO D)
def solicitar_mayuscula(mensaje:str) -> str:
    """
    Esta función verifica si una letra es unica entre la A y la Z.

        Recibe:
            mensaje (str): representa el mensaje a mostrar para el usuario al ingresar la letra
    
        Retorna:
            letra (str): representa la letra ya validada
    """

    bandera = False 

    while bandera == False:
        letra = input(mensaje)
        if len(letra) == 1: # Verificar que sea un único caracter
            bandera = determinar_AZ(letra) # Verifica si el caracter es una mayúscula
            
    return letra

#----------------------------------------   
def determinar_AZ(caracter: str) -> bool:
    """
    Esta función verifica si un caracter se encuentra entre A y la Z.
        
        Recibe:
            caracter (str): representa el caracter a evaluar
        
        Retorna:
            bandera (bool): indica si el caracter es o no una letra enta la A y la Z 
    """

    bandera = False
    codigo = ord(caracter)
    if (65 <= codigo <= 90): # Verifica si el carácter está en el rango de letras mayúsculas 
        bandera = True

    return bandera

#----------------------------------------
def buscar_dato(lista:list, dato:str)->bool:
    """
    Esta función verifica si un dato se encuentra o no en una lista.
        
        Recibe:
            lista (list): representa la lista en la cual buscar el dato
            dato (str): representa el dato a buscar en la lista
        Retorna:
            coincidencia (bool): indica si el dato se encontró o no en la lista 
    """
    
    coincidencia = False
    if len(dato) > 0:
        for i in range(len(lista)):
            if dato == lista[i]:
                coincidencia = True
                break
    return coincidencia

#----------------------------------------
def buscar_indices_dato(lista:list, dato:str)->list:
    """
    Esta función muestra los índices en los que se encuentra un dato en una lista.
        
        Recibe:
            lista (list): representa la lista en la cual buscar los indices del dato
            dato (str): representa el dato a buscar en la lista
        
        Retorna:
            indices (list): representa el o los índices en los que se encuenta el dato 
    """

    indices = []
    for i in range(len(lista)):
        if dato == lista[i]:
            indices += [i]
    return indices
        
#---------------------------------------------------------------------------------

# PUNTO E)
def ordenar_lista(lista:list, criterio:str):
    """
    Esta función ordena una lista ascendentemente o descendentemente segun el criterio.
        
        Recibe:
            lista (list): representa la lista a ordenar
            criterio (str): representa el criterio que se utilizara para ordenar la lista
    """

    for i in range(len(lista)-1):
        for j in range(i + 1,len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                aux = lista[i] 
                lista[i] = lista[j]
                lista[j] = aux

#----------------------------------------
def validar_orden(mensaje:str)-> str:
    """
    Esta función valida que el orden ingesado sea ASC o DESC
        
        Recibe:
            mensaje str): representa el mensaje para solicitar el orden
    
        Retorna:
            orden (list): representa el orden ya validado
    """

    orden = input(mensaje)
    while orden != "ASC" and orden != "DESC":
        orden = input(mensaje)
    return orden

#----------------------------------------
def copiar_lista(lista:list)->list:
    """
    Esta función genera una copia de una lista
        
        Recibe:
           lista (list): representa la lista a copiar  

        Retorna:
            copia_lista (list): representa la copia de la lista *lista 
    """

    copia_lista = []
    for i in lista:
        copia_lista += [i]
    return copia_lista


def ordenar_y_mostrar_copia_de_lista_en_orden(lista:list, mensaje:str):
    """
    Esta función genera una copia de una lista, la ordena según un criterio y la muestra por consola
        
        Recibe:
           lista (list): representa la lista a copiar 
           mensaje (str): representa el mensaje para que el usuario ingrese el criterio por el cual ordenar la lista
           
    """

    criterio = validar_orden(mensaje)
    copia_lista = copiar_lista(lista)
    ordenar_lista(copia_lista, criterio)
    print(f"\nLista de mayúsculas ordenada en orden {criterio}:\n")
    mostrar_lista(copia_lista)
#---------------------------------------------------------------------------------

# PUNTO G)
def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:int) -> list:
    """
    Esta función crea una matriz 
        
        Recibe:
           cantidad_filas (int): representa la cantidad de filas de la matriz
           cantidad_columnas (int): representa la cantidad de columnas de la matriz
           valor_inicial (int): representa el valor con el que se inicializa cada elemento de la matriz

        Retorna:
            matriz (list): representa la matriz ya creada
    """

    matriz = []
    for _ in range(cantidad_filas): 
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#----------------------------------------
def cargar_matriz_num_aleatorios(matriz:list):
    """
    Esta función carga una matriz con numeros enteros aleatorios
        
        Recibe:
           matriz (list): representa la matriz a cargar       
    """

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]= random.randint(1,9)

#---------------------------------------------------------------------------------

# PUNTO H)
def mostrar_matriz(matriz: list) -> list:
    """
    Esta función muestra por consola la matriz pasada por parámetro
        
        Recibe:
           matriz (list): representa la matriz a mostar        
    """
    
    for i in range(len(matriz)):
        print("| ", end="") # Separadores del inicio de la fila
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ") # Separadores de columnas
        print("")  # Espacio entre filas para mejor lectura

        if i < len(matriz) - 1:  # Evita poner "-" debajo de la última fila
            print("----" * len(matriz[i]))  # Separadores de filas