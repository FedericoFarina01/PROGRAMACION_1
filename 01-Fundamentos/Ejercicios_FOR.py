# 1) Mostrar los números ascendentes desde el 1 al 10

for i in range(1, 10):
    print(i)


# 2) Mostrar los números descendentes desde el 10 al 1

for i in range(10, 0, -1):
    print(i)


# 3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("Ingrese un número: "))

for i in range(numero):
    print(i)


# 4) Ingresar un número y mostrar la tabla de multiplicar de ese número. 
# Por ejemplo si se ingresa el numero 5:

numero = int(input("Ingresa un número: "))

for i in range(11):
    print(f"{numero} * {i} = {numero * i}")
    
    

# 5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.

acumulador = 0

for i in range(10):
    numero = int(input("Ingresa un numero: "))
    if numero == 0:
        break
    acumulador += numero

promedio = acumulador / 10

print(f"Suma: {acumulador}\nPromedio: {promedio}")



# 6) Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

print('--- Opcion 1 ---')

for i in range(1, 11):
    if i % 3 == 0:
        print(i)
        
print('--- Opcion 2 ---')

for i in range(3, 11, 3):
    print(i)


# 7) Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
for i in range(2, 51, 2):
    print(i)


# 8) Realizar un programa que permita mostrar una pirámide de números. Por
# ejemplo: si se ingresa el numero 5, la salida del programa será la
# siguiente:

"""
1
12
123
1234
12345
"""

numero = int(input('Ingresa un número: '))
numero_string = ""

for i in range(1, numero + 1):
    numero_string += str(i)
    print(numero_string)


# 9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# Mostrar la cantidad de divisores encontrados.

divisores_encontrados = 0

numero = int(input('Ingresa un número: '))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        divisores_encontrados += 1

print(f"Divisores encontrados: {divisores_encontrados}")



# 10) Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingresa un numero: "))
divisores_encontrados = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores_encontrados += 1

if divisores_encontrados == 2:
    print("Es primo")


# 11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron


numero = int(input("Ingresa un número: "))
primos_encontrados = 0

for i in range(2, numero + 1):
    divisores_encontrados = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisores_encontrados += 1
    if divisores_encontrados == 2:
        print(f"{i} es primo")
        primos_encontrados += 1

print(f"Se encontraron {primos_encontrados} números primos.")

    
    