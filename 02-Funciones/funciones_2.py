# 1) Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.
def determinar_par_impar(numero:int) -> bool:
    """
    Esta función determina si un número es par o impar.
        Recibe:
            numero (int): representa el número a analizar si es par o impar
        Devuelve:
            par_impar (bool): True si el número es par - False si el número es impar
    """
    if numero % 2 == 0:
        par_impar = True

    else:
        par_impar = False

    return par_impar

# 2) Desarrollar una función que permita validar un número entero. Deberá recibir por parámetro el número a validar, y dos números que representan el rango mínimo y máximo permitido. Devolverá True en caso de ser válido, False de lo contrario.
def validar_numero_entero_en_rango(numero:int, minimo:int, maximo:int) -> bool:
    """
    La función determina si un número se encuentra dentro de un rango determinado por dos enteros.
        Recibe:
            numero (int): representa el número a analizar
            minimo (int): representa el mínimo del rango en el cual se analiza el número
            maximo (int): representa el máximo del rango en el cual se analiza el número
        Devuelve:
            retorno (bool): True si el número se encuentra dentro del rango analizado, False en caso de que no y None si alguno de los parámetros no son enteros (int)
    """
    retorno = None
    
    if type(numero) == int and type(minimo) == int and type(maximo) == int: # Validación
        if numero >= minimo and numero <= maximo: # Si número está dentro del rango de mínimo y máximo
            retorno = True
        
        else:
            retorno = False

    return retorno

# 3) Desarrollar una función que se encargue de solicitar un número entero al usuario, validarlo (reutilizando la función del punto anterior) y retornar el número validado y transformado a entero. Deberá recibir por parámetro un mensaje que se le mostrará al usuario y los rangos de validación.
def solicitar_numero_entero(mensaje:str, minimo:int, maximo:int) -> int:
    """
    Esta función verifica si un número ingresado por el usuario es un entero dentro de un rango entre otros dos números enteros.
        Recibe:
            mensaje (str): representa el mensaje a mostrar para el usuario al ingresar el número
            minimo (int): representa el mínimo del rango en el cual se analiza el número
            maximo (int): representa el maximo del rango en el cual se analiza el número
        Devuelve:
            numero (int): representa ingresado ya validado
    """

    bandera = False # La inicializamos en False para forzarla a entrar en el siguiente While

    while bandera == False:
        numero = input(mensaje)
        bandera = verificar_digito(numero) # Función para verificar si se puede castear a entero, devuelve True si se puede

    numero = int(numero) # Se castea luego de verificar

    while validar_numero_entero_en_rango(numero, minimo, maximo) != True:
        bandera = False
        while bandera == False:
            numero = input(mensaje)
            bandera = verificar_digito(numero) 

        numero = int(numero) # Se castea luego de verificar
        # numero = int(input(mensaje))

    return numero


def verificar_digito(string:str) -> bool:
    """
    Esta funcion verifica si todos los digitos de una cadena son numeros enteros
        Recibe:
            cadena (str): Cadena que se va a iterar para validar sus caracteres.
        Retorna:
            retorno (bool):
                True: Si toda la cadena son digitos del 0 al 9
                False: Si la cadena tiene un caracter que no sea numerico.
    """
    retorno = True
    for digito in string:
        if ord(digito) < 48 or ord(digito) > 57:
            retorno = False
            break

    return retorno

#prueba = solicitar_numero_entero("Ingrese un número: ", 1, 10)
#print(prueba, type(prueba))


"""4) Desarrollar una función que se encargue de solicitar una cadena de caracteres al usuario, validarla y
retornar la misma. Deberá recibir como parámetro un mensaje para indicarle al usuario y 1, 2 o 3 cadenas
de caracteres que representarán las opciones válidas de ingreso"""
def solicitar_cadena(mensaje:str, cadena:str) -> str:
    """
    Esta función verifica si una cadena de caracteres es valida.
        Recibe:
            mensaje (str): representa el mensaje a mostrar para el usuario al ingresar la cadena
            cadena (str) : representa una opcion valida de ingreso
        Devuelve:
            cadena (str): representa la cadena ya validada
    """

    bandera = False # La inicializamos en False para forzarla a entrar en el siguiente While

    while bandera == False:
        cadena = input(mensaje)
        bandera = verificar_cadena(cadena) # Función para verificar si todos los caracteres son letras


def verificar_cadena(string:str) -> bool:
    """
    Esta funcion verifica si todos los digitos de una cadena son letras.
        Recibe:
            string (str): Cadena que se va a iterar para validar sus caracteres.
        Retorna:
            retorno (bool):
                True: Si toda la cadena son letras
                False: Si la cadena tiene un caracter que no sea letra.
    """
    retorno = True
    for caracter in string:
        if ord(caracter) < 65 or ord(caracter) > 122:
            retorno = False
            break

    return retorno


"""
5) Desarrollar una función que se encargue de medir el largo de una cadena de caracteres, deberá recibir por
parámetro la cadena de caracteres a evaluar y devolverá un número entero representando la longitud de
la cadena recibida
"""
def medir_cadena (cadena:str)->int:
    contador = 0
    for caracter in cadena:
        contador += 1

    return (contador)

resultado = medir_cadena("123")
print(resultado)


"""
6) Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo deberá devolver un True, de lo contrario False.
"""
def determinar_primo(numero:int)-> bool:
    primo = True
    divisores_encontrados = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            divisores_encontrados += 1

    if divisores_encontrados >= 3:
        primo = False

    return (primo)


"""
7) Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del
factorial de ese número.
"""
def calcular_factorial(numero:int)-> int:
    factorial = 1
    for i in range(numero,1,-1):
        factorial *= i

    return (factorial)


"""
8) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a...z o
A...Z, en caso afirmativo devolverá True, de lo contrario False.
"""
def determinar_az_AZ(caracter: str) -> bool:
    # Verifica si el carácter está en el rango de letras mayúsculas o minúsculas
    codigo = ord(caracter)
    bandera = False
    if (65 <= codigo <= 90) or (97 <= codigo <= 122):
        bandera = True

    return(bandera)


"""
9) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre 0...9,
devolverá un valor boolean indicando si el carácter recibido es numérico o no.
"""
def determinar_09(caracter:str)-> bool:
    codigo = ord(caracter)
    bandera = False
    if (48 <= codigo <= 57):
        bandera = True

    return(bandera)


"""
10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres
(se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o
mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.
"""
def verificar_DNI(dni:str)->bool:
    valido = False
    largo_dni = 0
    for caracter in dni:
        largo_dni += 1
    if 6 <= largo_dni <= 8:
        valido = True

    return(valido)


"""
11) Desarrollar una función que complete el número de DNI de una persona. Recibirá una cadena de
caracteres (se asume que solamente contiene caracteres numéricos), deberá medirla y completar con ceros
a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. Ej: Se ingresa
“123456”, y devolverá “00123456”.
"""
def completar_DNI(dni: str) -> str:
    largo_dni = len(dni)
    diferencia = 8 - largo_dni

    if largo_dni < 8:
        dni_completo = "0" * diferencia + dni
    else:
        dni_completo = dni

    return dni_completo

print(completar_DNI("4319784"))


"""
12) Desarrollar una función que transforme una cadena de caracteres numérica a su equivalente en letras.
Recibirá por parámetro la cadena a transformar y devolverá el resultado en letras. Ej: “987” ->
"novecientos ochenta y siete". Como máximo tomar el número más grande de 3 dígitos.
"""
def pasar_unidades(numero:str)->str:
    resultado = ""

    if numero == "1":
        resultado = "uno"
    elif numero == "2":
        resultado = "dos"
    elif numero == "3":
        resultado = "tres"
    elif numero == "4":
        resultado = "cuatro"
    elif numero == "5":
        resultado = "cinco"
    elif numero == "6":
        resultado = "seis"
    elif numero == "7":
        resultado = "siete"
    elif numero == "8":
        resultado = "ocho"
    elif numero == "9":
        resultado = "nueve"
    else:
        resultado = "cero"
    
    return resultado

def pasar_decenas(numero:str, unidad:str="0")->str:
    resultado = ""

    if numero == "1":
        resultado = "diez"
    elif numero == "2":
        resultado = "veinte"
    elif numero == "3":
        resultado = "treinta"
    elif numero == "4":
        resultado = "cuarenta"
    elif numero == "5":
        resultado = "cincuenta"
    elif numero == "6":
        resultado = "sesenta"
    elif numero == "7":
        resultado = "setenta"
    elif numero == "8":
        resultado = "ochenta"
    elif numero == "9":
        resultado = "noventa"
    
    return resultado

def pasar_centenas(numero:str, redondo:bool=False)->str:
    resultado = ""

    match numero:
        case "1":
            resultado = "ciento"
        case "2":
            resultado = "doscientos"
        case "3":
            resultado = "trescientos"
        case "4":
            resultado = "cuatrocientos"
        case "5":
            resultado = "quinientos"
        case "6":
            resultado = "seiscientos"
        case "7":
            resultado = "setecientos"
        case "8":
            resultado = "ochocientos"
        case "9":
            resultado = "novecientos"
        
    if redondo == True and numero == "1":
        resultado = "cien"
    
    return resultado

def convertir_numero_a_letra(cadena:str)->str:
    largo_cadena = medir_cadena(cadena)
    cadena = int(cadena)

    centena = str(cadena//100)
    cadena = cadena % 100
    decena = str(cadena //10)
    unidad = str(cadena % 10)

    match largo_cadena:
        case 1:
            resultado = pasar_unidades(unidad)
        case 2:
            resultado = pasar_decenas(decena)
            if unidad != "0":
                resultado = resultado + " y " + pasar_unidades(unidad)
        case 3:
            if decena == "0":
                if unidad == "0":
                    resultado = pasar_centenas(centena, True)
            else:
                resultado = pasar_centenas(centena)
                resultado = resultado + " " + pasar_decenas(decena)
                if unidad != "0":
                    resultado = resultado + " y " + pasar_unidades(unidad)

    return resultado

print(convertir_numero_a_letra("55"))