""" 1) Desarrollar función calcular_fibonacci.
Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
Funcionalidad: La función deberá calcular el número n-ésimo en la sucesión de Fibonacci.
Si n = 0, deberá devolver 0.
Si n = 1, deberá devolver 1.
Para cualquier n > 1, el resultado será la suma de los dos números anteriores de la secuencia.
Retorno: El resultado calculado previamente.
Por ejemplo:
● f 0 = 0
● f 1 = 1
● f 2 = 1
● f 3 = 2
● f 4 = 3
● f 5 = 5
● f 6 = 8
"""

def calcular_fibonacci(numero:int)-> int:
    if numero < 2:
        resultado = numero

    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

    return resultado

print(calcular_fibonacci(7))

"""
2) Desarrollar función mostrar_serie_fibonacci.
Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
Funcionalidad: La función deberá mostrar la secuencia completa hasta el número n-ésimo en la sucesión de
Fibonacci, incluyendo a este último.
Retorno: None """

def mostrar_serie_fibonacci(numero:int)->None:
    for i in range(0, numero + 1):
        print(f"f{1} = {calcular_fibonacci(i)}")

mostrar_serie_fibonacci(7)