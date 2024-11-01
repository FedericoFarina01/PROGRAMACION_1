# 1) Desarrolle una función que cuente las letras vocales de una cadena de caracteres pasada por
# parámetro.

def contar_vocales(cadena:str, caracteres_a_contar: list) -> int:
    resultado = cadena.lower()
    contador = 0
    for i in range(len(caracteres_a_contar)):
        contador += resultado.count(caracteres_a_contar[i])
    return contador

# print(contar_vocales("Hola mundo", ["a", "e", "i", "o", "u"]))

# 2) Desarrolle una función que reciba una cadena de caracteres y un separador por parámetro,
# luego limpiara los espacio vacíos que se encuentren al principio y al final de la cadena de
# caracteres y reemplazará los espacios en el medio de la misma utilizando el separador
# recibido.

def limpiar_espacios_vacios(cadena_a_limpiar:str, separador:str, caracter_a_limpiar:str) -> str:
    cadena_limpia = cadena_a_limpiar.strip(caracter_a_limpiar)
    cadena_reemplazada = cadena_limpia.replace(" ", separador)
    return cadena_reemplazada

# print(limpiar_espacios_vacios(" hola mundo   ", "_", " " ))


# 3) Desarrolle una función que cuente los caracteres de una cadena de caracteres con excepción
# del espacio.

def contar_caracteres(cadena:str, excepcion:str)->int:
    """
    """
    #resultado = cadena.replace(excepcion, "")
    #cadena_limpia = len(resultado)
    #return cadena_limpia
    resultado= cadena.count(excepcion)
    contador = len(cadena)- resultado
    return contador


#print(contar_caracteres("Hol a m un do "," "))


# 4) Desarrolle una función que cuente las palabras de una cadena de caracteres.

def contar_palabras_de_cadena(cadena:str,excepcion:str)->int:
    """
    """
    palabras = cadena.strip(excepcion)
    resultado= palabras.split(excepcion)
    return len(resultado)


print(contar_palabras_de_cadena("  Hola mundo ", " "))


# 5) Desarrolle la función “normalizar_texto()”, que recibirá por parámetro una cadena y un
# criterio, la misma deberá limpiar la cadena recibida de cualquier espacio extra que se
# encuentre al principio o al final de la cadena, y dependiendo del criterio recibido la
# transformará a mayúsculas, minúsculas o un título.

def normalizar_texto(cadena:str, criterio:str, caracter_limpiar:str = " ") -> str:
    """
    """
    cadena = cadena.strip(caracter_limpiar)

    match criterio:
        case "minusculas":
            cadena = cadena.lower()
        case "mayusculas":
            cadena = cadena.upper()
        case "capitalize":
            cadena = cadena.capitalize()
        case "titulo":
            cadena = cadena.title()

    return cadena

# cadena = "    hola mUNdo MESSI              "

# print(normalizar_texto(cadena, "capitalize"))

# 6) Desarrolle la función “personalizar_titulo()”, que recibirá por parámetro una cadena y le dará
# formato de título, con excepción de las siguientes palabras que deben aparecer en letra
# minúscula: ‘y’, ‘el’, ‘la’, ‘de’.

def personalizar_titulo(cadena:str, excepciones:list, separador:str = " ") -> str:
    """
    """
    cadena = cadena.lower()
    lista_palabras = cadena.split(separador)

    for i in range(len(lista_palabras)):
        if lista_palabras[i] not in excepciones:
            lista_palabras[i] = lista_palabras[i].title()

    cadena = separador.join(lista_palabras)

    return cadena
    
cadena = "campeones DE america y deL mundo"
lista_excepciones = ["y", "el", "la", "de", "del"]

print(personalizar_titulo(cadena, lista_excepciones))


"""
Ejercicio 7:
Desarrolle la función “resumir_texto()”, que recibirá por parámetro una cadena de caracteres
larga y un entero que representa la cantidad máxima de palabras. Si la cadena supera la
cantidad máxima de palabras deberá retornar la cadena con la cantidad máxima de palabras
y tres puntos al final “...”, si no lo supera, devolverá la cadena original si modificarla.
"""
def contar_palabras_de_cadena(cadena:str, exepcion:str) -> str:
    """_summary_

    Args:
        cadena (str): _description_

    Returns:
        str: _description_
    """

    # palabras = cadena.strip()split()
    # return len(palabras)

    palabras = cadena.strip(exepcion)
    resultado = palabras.split(exepcion)
    return len(resultado)

def resumir_texto(cadena:str, maximo_palabras:int, separador:str=" ") -> str:
    """_summary_

    Args:
        cadena (str): _description_
        maximo_palabras (int): _description_

    Returns:
        str: _description_
    """
    if contar_palabras_de_cadena(cadena, separador) > maximo_palabras:
        resultado = cadena.split(separador, maximo_palabras)
        #"Hola mundo juan gol hola mudo"
        resultado[-1] = "..."
        resultado = separador.join(resultado)
    else: 
        resultado = cadena
    return resultado

print(resumir_texto("Hola mundo juan gol hola mudo", 10))

