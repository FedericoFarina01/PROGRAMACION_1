# OPERADORES TERNARIOS:
x = 43
resultado = "es la respuesta" if x == 43 else "anduviste cerca"
print(resultado)

numero = 44

resultado = "es la respuesta" if numero == 43 else "anduviste cerca"
def es_par(numero):
    return "ES PAR" if numero % 2 == 0 else "ES IMPAR"

if numero == 43:
    resultado = "es la respuesta"
    print("ADIVINASTE!!")     
else:
    resultado = "anduviste cerca"
print(resultado)

#===================================================================

# LAMBDA:
print((lambda num: num == 5)(5))

print((lambda num: "es par" if num % 2 == 0 else "no es par")(5))

mi_funcion = lambda mi_variable: mi_variable % 2 == 0
print(mi_funcion(5))

print((lambda num: num == 5)(5))

# Funcion Anonima utilizando operadores ternarios:

print((lambda num, str: str if num % 2 == 0 else "no es par")(4, "ES PAR"))

# Parametros Actuales:
print(input("Ingrese un nombre: ")) # Invocacion de la funcion print, por parametro recibe la invocacion de otra funcion.


# Funcion como parametro Formal:
def es_par(num:int)->bool:
    return num % 2 == 0

def es_primo(num:int)->bool:
# Logica que determina si un numero es primo
    pass

def filtrar_lista(lista, mi_funcion)->list:
    lista_pares = []
    for i in range(len(lista)):
        if mi_funcion(lista[i]) == True:
            lista_pares.append(lista[i])
    return lista_pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = filtrar_lista(lista_numeros, es_par)
lista_primos = filtrar_lista(lista_numeros, es_primo)

print(lista_pares)

mi_funcion = es_par
print(mi_funcion(5))


# Sort con funciones por parametro
lista = [4, 3, 2, 7, 5, 1, 6]
lista.sort() # Por defecto -> ASC 
lista.sort(reverse=True) # reverse -> DESC

def ordenar_criterio_custom(dato:int):
    return True if dato % 2 == 0 else False
 
lista.sort(key=ordenar_criterio_custom, reverse=True) # ASC
print(lista) # Prohibido

#===================================================================

# JSON

import json

mi_diccionario = {"nombre": "Valeriy", "edad": 35, "es_profe": True, "notas": [1, 2, 3, 4]}

with open("test.json", "w") as archivo:
    json.dump(mi_diccionario, archivo, indent=4)

with open("test.json", "r") as archivo:
    data = json.load(archivo)
print(data)



# ARCHIVOS (existen archivos de texto y binarios):

# Texto:
# .txt -> extension comun de archivos de texto. (Algoritmicamente)
# .CSV -> Comma Separated Values. (Algoritmicamente)
# .JSON -> JavaScript Object Notation. (Metodos)


# Abrir un archivo v1:
# Primer parametro del open es la RUTA del archivo, segundo parametro es el modo (r, w, a)
# Ruta (Path) relativa -> relativa a la ubicacion actual
# Ruta absoluta -> ruta completa del archivo 
# C: clase/mi_archivo.py
mi_archivo = open("C:/Users/valer/OneDrive/Escritorio/Curso de Ingreso/mi_archivo.txt", "w")
mi_archivo.close()


# # Abrir un archivo v2.0:

mi_ruta = "Programacion_I_2C/Clase_16/mi_archivo.txt"
MODO_ESCRITURA = "w" # Constante
MODO_LECTURA = "r"
MODO_APPEND = "a"
with open(mi_ruta, MODO_ESCRITURA) as mi_archivo:
     # Bloque de codigo con el archivo abierto
    pass

print("Termino mi programa")



mi_ruta = "Programacion_I_2C/Clase_16/mi_archivo.txt" # Ruta relativa guardada en una variable
MODO_ESCRITURA = "w" # Constante
MODO_LECTURA = "r"
MODO_APPEND = "a"
with open(mi_ruta, MODO_LECTURA) as mi_archivo:
     # Bloque de codigo con el archivo abierto
      for dato in mi_archivo:
        print(dato, end="")
        datos_de_mi_archivo = mi_archivo.read()

print(datos_de_mi_archivo) # Estos datos, estan guardados en la memoria RAM

print("\nTermino mi programa")


mi_ruta = "Programacion_I_2C/Clase_16/mi_archivo3.txt" # Ruta relativa guardada en una variable
MODO_ESCRITURA = "w" # Constante
MODO_LECTURA = "r"
MODO_APPEND = "a"
with open(mi_ruta, MODO_LECTURA) as mi_archivo:
    mi_archivo.write("\nTEST")
    mi_archivo.writelines(["5\n", "3\n", "Pepe\n", "Hola\n"])
    for linea in mi_archivo.readlines(): # lectura de linea por linea
        print(linea, end="")


# CSV (Se maneja algoritmicamente, al igual que los .txt)
lista = [6, 3, 6, 7, 8, 1, 2, -5]
with open("Programacion_I_2C/Clase_16/numeros.csv", MODO_ESCRITURA) as archivo:
      dato_a_escribir = ""
      for i in range(len(lista)):
          if i != len(lista) - 1:
              dato_a_escribir += str(lista[i]) + ","
          else:
              dato_a_escribir += str(lista[i])
      archivo.write(dato_a_escribir)
      archivo.writelines(str(lista))

print("Se termino de escribir al archivo y se cerro el programa")




# JSON
import json
# Metodos del json: load / dump
lista = [{"nombre": "Juan", "edad": 35}, {"nombre": "Pepe", "edad": 40}]
diccionario = {"nombre": "Juan", "edad": 35}

with open("Programacion_I_2C/Clase_16/personas.json", "w") as archivo:
    json.dump(diccionario, archivo, indent=4)

with open("Programacion_I_2C/Clase_16/personas.json", "r") as archivo:
    datos_leidos = json.load(archivo)
    # pueden trabajar esos datos antes de cerrar el archivo

print(datos_leidos, type(datos_leidos["edad"]))
