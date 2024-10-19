def sumar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la suma de dos numeros.
    Recibe:
    num_a (int) seria el primer numero a sumar
    num_b (int) seria el segundo numero a sumar
    Devuelve:
    suma (int) seria la suma de los numeros
    '''

    suma = num_a + num_b
    return suma

#resultado = sumar(5,6)
#print(resultado)

def restar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la resta de dos numeros.
    Recibe:
    num_a (int) seria el primer numero a restar
    num_b (int) seria el segundo numero a restar
    Devuelve:
    suma (int) seria la resta de los numeros
    '''

    resta = num_a - num_b
    return resta

#resultado = restar(5,6)
#print(resultado)


def multiplicar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la multiplicacion de dos numeros.
    Recibe:
    num_a (int) seria el primer numero a multiplicar
    num_b (int) seria el segundo numero a multiplicar
    Devuelve:
    suma (int) seria la multiplicacion de los numeros
    '''

    multiplicacion = num_a * num_b
    return multiplicacion

#resultado = multiplicar(5,6)
#print(resultado)



def dividir(num_a:float, num_b:float)->float:
    '''
    Esta funcion calcula la division de dos numeros.
    Recibe:
    num_a (int) seria el primer numero a dividir
    num_b (int) seria el segundo numero a dividir
    Devuelve:
    suma (int) seria la suma de los numeros
    '''
    division = None
    if num_b != 0:
        division = num_a / num_b    
    return division

#resultado = dividir(5,6)
#print(resultado)


def calcular_resto(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula el resto de dos numeros.
    Recibe:
    num_a (int) seria el primer numero 
    num_b (int) seria el segundo numero
    Devuelve:
    suma (int) seria el resto de los numeros
    '''
    resto = None
    if num_b != 0: 
        resto = num_a % num_b
    return resto

#resultado = calcular_resto(5,6)
#print(resultado)