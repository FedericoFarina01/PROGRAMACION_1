# 1) Desarrollar una función que reciba como parámetros fecha actual y fecha de nacimiento; y retorne la edad.

def extraer_string(cadena:str, desde:int, hasta:int) -> str:
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

# extraer_string("02-09-2024", 7, 10)
def mostrar_edad(fecha_nacimiento:str, fecha_actual:str) -> int:
    '''
    pide una fecha de nacimiento y fecha actual
        muestra la edad actual del usuario    
    '''
    # (02-09-2024)
    dia_nacimiento = extraer_string(fecha_nacimiento, 1, 2)
    mes_nacimiento = extraer_string(fecha_nacimiento, 4, 5)
    año_nacimiento = extraer_string(fecha_nacimiento, 7, 10)

    dia_actual = extraer_string(fecha_actual, 1, 2)
    mes_actual = extraer_string(fecha_actual, 4, 5)
    año_actual = extraer_string(fecha_actual, 7, 10)

    edad = int(año_actual) - int(año_nacimiento)

    if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1

    return edad
    
print(mostrar_edad("04-11-2000", "02-09-2024"))


    # dia_nacimiento = int(fecha_nacimiento[0] + fecha_nacimiento[1]) 
    # mes_nacimiento = int(fecha_nacimiento[3] + fecha_nacimiento[4])
    # año_nacimiento = int(fecha_nacimiento[6] + fecha_nacimiento[7] + fecha_nacimiento[8] + fecha_nacimiento[9])

    # dia_actual = int(fecha_actual[0] + fecha_actual[1])
    # mes_actual = int(fecha_actual[3] + fecha_actual[4])
    # año_actual = int(fecha_actual[6] + fecha_actual[7] + fecha_actual[8] + fecha_actual[9])

    # edad_usuario = año_actual - año_nacimiento

    # if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    #     edad_usuario -= 1

    # mensaje = f"su edad actual es: {edad_usuario}"

# fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ")
# fecha_actual = input("Ingrese la fecha actual (DD-MM-AAAA): ")

# print(mostrar_edad(fecha_nacimiento, fecha_actual))


""" # 2) Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
respectivamente """

# 2) Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
# letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
# respectivamente.

def extraer_string(cadena:str, desde:int, hasta:int) -> str:
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

def mostrar_vehiculo(patente:str) -> str:
    '''
    funcion que recibe una patente como parametro 
    retorna tipo de vehiculo
    '''
    letra1 = extraer_string(patente, 1, 1)
    
    if ord(letra1) > 47 and ord(letra1) < 58:
        vehiculo = "Moto"
    else:
        vehiculo = "Auto"

    return vehiculo

print(mostrar_vehiculo("192 AFG"))
print(mostrar_vehiculo("AFG 192"))
print("\n")
print("\n")
# ABC 123
# 123 ABC

""" 3) Desarrollar una función que reciba como parametros numero de DNI y
[MASCULINO|FEMENINO|EMPRESA]. Deberá retornar el CUIL/CUIT formado por:
CUIL/T: Son 11 números en total:
XY – 12345678 – Z
XY: Indican el tipo (Masculino, Femenino o una empresa)
12345678: Número de DNI
Z: Código Verificador
Algoritmo: Se determina XY con las siguientes reglas:
Masculino: 20
Femenio: 27
Empresa: 30
Se multiplica XY 12345678 por un número de forma separada:
X * 5
Y * 4
1 * 3
2 * 2
3 * 7
4 * 6
5 * 5
6 * 4
7 * 3
8 * 2
Se suman dichos resultados. El resultado obtenido se divide por 11. De esa división se obtiene un Resto que
determina Z.
Si el resto es 0 = Entonces Z = 0.
Si el resto es 1 = Entonces se aplica la siguiente regla:
*Si es hombre: Z = 9 y XY pasa a ser 23
*Si es mujer: Z = 4 y XY pasa a ser 23
Caso contrario Z pasa a ser (11 - Resto).
2
Programación I
David Fernández - Valeriy Pavlov
Funciones
Ejemplo de Cálculo de CUIL CUIT:
Masculino DNI 12345678
1-Determinar el Tipo
XY es 20
Hacemos el cálculo
2 * 5=10
0 * 4=0
1 * 3=3
2 * 2=4
3 * 7=21
4 * 6=24
5 * 5=25
6 * 4=24
7 * 3=21
8 * 2=16
Realizamos la suma de (10+0+3+4+21+24+25+24+21+16) = 148
Dividimos por 11 para obtener Z (el código verificador)
148 / 11 = 13,4545 —> 13 (Redondeo)
Obtenemos el resto de la división:
148 – (13*11) = 5
Determinamos Z:
11 - 5 = 6
Conclusión: CUIL-CUIT 20-12345678-6 """

def generar_cuil(dni:int, tipo:str) -> str:
    '''
    '''
    match tipo:
        case "masculino":
            xy = "20"
        case "femenino":
            xy = "27"
        case "empresa":
            xy = "30"
            
    documento_aux = xy + str(dni)
    mult = 5
    acumulador = 0

    for digito in documento_aux:
        acumulador += (int(digito) * mult)
        mult -= 1
        if mult == 1:
            mult = 7

    resto = acumulador % 11

    if resto == 0:
        digito_verificador = resto
    elif resto == 1:
        if tipo == "masculino":
            digito_verificador = 9
        elif tipo == "femenino":
            digito_verificador = 4
        xy = 23
    else:
        digito_verificador = 11 - resto
        
    cuil = f"{xy}-{dni}-{digito_verificador}"

    return cuil

print(generar_cuil(12345678, "masculino"))