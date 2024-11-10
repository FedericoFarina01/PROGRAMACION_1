from funciones import *
import json

# Ejericios archivos:

# Ejercicio 1:
"""
1) Agregar las siguientes funciones al menú del trabajo práctico sobre diccionarios:
- Desarrolle una función que permite guardar una lista de diccionarios en formato JSON (utilizar esta
función como opción 11 y añadir guardado automático a la opción de salir, con confirmación por parte del
usuario).
- Desarrolle una función que permite leer una lista de diccionarios desde un archivo JSON (se carga
automáticamente al ingresar a la opción de Altas).
"""



"""
Desarrolle un programa con un menú que contenga los siguientes ítems y una opción para salir:
1) Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y
segundo examen parcial).
2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
donde cada fila representa un alumno y cada columna representa uno de sus datos.
3) Modificación: Desarrolle una función que permita calcular el promedio de calificaciones a partir de
una lista de alumnos. Recibe una lista de diccionarios por parámetro, calcula el promedio y lo agrega
como un ítem más al diccionario.
4) Desarrolle una función que informe por cada alumno de la lista su estado académico (promedio de 1 al
4: desaprobado, 4 o 5: aprobado, y 6 o más: promocionado).
5) Desarrolle una función que informe las notas y el promedio del alumno cuyo nombre recibe por
parámetro, en caso de no encontrarlo deberá imprimir un mensaje de error.
6) Baja Física: Desarrolle una función que pueda eliminar a un alumno de la lista de alumnos. El alumno
a eliminar deberá seleccionarlo el usuario por terminal, validar que exista antes de eliminarlo, y en
caso de que no exista mostrar un mensaje de error.
7) Baja Lógica: Desarrolle una función que pueda dar de baja lógicamente a un alumno de la lista.
Deberá recibir por parámetro el nombre del alumno a eliminar y agregarle un estado (bool) activo o
inactivo. Modificar la función que muestra los alumnos haciendo que ignore a todos los alumnos
inactivos.
8) Desarrolle una función que busque al alumno con el mejor o con el peor promedio. Informar sus nombres y sus respectivos promedios.
9) Desarrolle una función que ordene a los alumnos por promedio ASC/DESC.
10) Desarrolle una función que calcule e informe la cantidad de alumnos según su estado académico
(desaprobado, aprobado o promocionado).
"""


def menu():
    menu = '''
1) Cargar datos
2) Mostrar datos
3) Calcular promedio
4) Informar estado académico
5) Buscar alumno
6) Baja física
7) Baja Logica
9) Ordenar alumnos
11) Guardar archivos
0) Salir del programa

Ingrese una opcion: 
'''
    respuesta = "n"
    try:
        lista_de_alumnos = cargar_archivo_json("Ejercicios Programación I/Ejercicios_archivos/datos_alumnos.json")
    except:
        lista_de_alumnos = []

    while respuesta == "n":
        seleccionar_opcion = input(menu)

        match seleccionar_opcion:
            case "1":
                alumno = cargar_datos("nombre", "nota_1", "nota_2", "activo")
                lista_de_alumnos.append(alumno)
            case "2":
                mostrar_lista_alumnos(lista_de_alumnos)
            case "3":
                calcular_promedio(lista_de_alumnos, "promedio")
                mostrar_lista_alumnos(lista_de_alumnos)
            case "4":
                informar_estado_academico(lista_de_alumnos, "promedio")
            case "5":
                alumno_a_buscar = input("ingrese el nombre del alumno que busca: ")
                resultado_busqueda = buscar_alumno(lista_de_alumnos, alumno_a_buscar)
                if resultado_busqueda == None:
                    print(f"no se encontro el alumno de nombre {alumno_a_buscar}") 
                else:
                    mostrar_titulo(lista_de_alumnos)
                    mostrar_un_alumno(resultado_busqueda)
            case "6":
                alumno_a_eliminar = input("Ingrese el alumno a eliminar: ")
                borrar_alumno(lista_de_alumnos, alumno_a_eliminar)
            case "7":
                alumno_a_dar_de_baja = input("Ingrese el nombre a dar de baja: ")
                diccionario_a_dar_de_baja = buscar_alumno(lista_de_alumnos , alumno_a_dar_de_baja)
                if diccionario_a_dar_de_baja == None:
                    print(f"no se encontro el alumno de nombre {alumno_a_buscar}") 
                else:
                    diccionario_a_dar_de_baja.update({"activo":False})
                    print("Se desactivo al alumno", diccionario_a_dar_de_baja["nombre"])
            case "8": 
                pass
            case "9":
                calcular_promedio(lista_de_alumnos, "promedio")
                criterio = validar_criterio("Ingrese el criterio de ordenamiento (ASC/DESC): ", ["ASC", "DESC"])
                ordenar_alumnos(lista_de_alumnos, criterio, clave="promedio")
            case "10":
                pass
            case "11":
                guardar_archivo_json(lista_de_alumnos,"Ejercicios Programación I/Ejercicios_archivos/datos_alumnos.json" )
                print("Se guardaron los alumnos en el archivo json")
            case "0":
                confirmacion_guadardo_archivos = input("Desea guardar el archivo antes de salir del programa (s/n): ")
                if confirmacion_guadardo_archivos == "s":
                    guardar_archivo_json(lista_de_alumnos,"Ejercicios Programación I/Ejercicios_archivos/datos_alumnos.json" )
                    print("Se guardaron los alumnos en el archivo json")
                print("Cerrando programa")
                break
            case _:
                print("Opcion no valida, ingres un numero del 1 al 10")








"""
1) Agregar las siguientes funciones al menú del trabajo práctico sobre diccionarios:
- Desarrolle una función que permite guardar una lista de diccionarios en formato JSON (utilizar esta
función como opción 11 y añadir guardado automático a la opción de salir, con confirmación por parte del
usuario).
- Desarrolle una función que permite leer una lista de diccionarios desde un archivo JSON (se carga
automáticamente al ingresar a la opción de Altas).
"""

"""
Opción 11:
"""
def guardar_archivo_json(lista:list[dict], ruta:str):
    """
    """
    with open(ruta, "w") as mi_archivo:
        json.dump(lista, mi_archivo, indent = 4)


# Importar datos del archivo json al programa

def cargar_archivo_json(ruta:str)-> list[dict]:
    """
    """
    with open(ruta, "r") as mi_archivo:
        datos = json.load(mi_archivo)
    
    return datos


# 2) Desarrolle y pruebe las siguientes funciones en un archivo separado al de trabajo práctico sobre
# diccionarios:
# - Desarrolle una función que genere una matriz de 9 filas por 9 columnas con números aleatorios del 1
# al 9 inclusive.
import random

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any = None)->list:
    """
    """
    lista = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        lista += [fila]
    
    return lista

def generar_matriz_aleatoria(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1, 9)

mi_matriz = inicializar_matriz(9, 9)
#print(mi_matriz)
generar_matriz_aleatoria(mi_matriz)
#print(mi_matriz)

# - Desarrolle una función que guarde la matriz generada aleatoriamente en un archivo con formato CSV,
# donde las columnas están separadas por comas y las filas por saltos de línea (\n).

# def guardar_archivo_CSV(matriz:list, ruta:str):
#     with open(ruta, "w") as archivo:
#         for i in range(len(matriz)):
#             for j in range(len(matriz[i])):
#                 if j == len(matriz[i])-1:
#                     dato_a_escribir = str(matriz[i][j])+"\n"
#                 else:
#                     dato_a_escribir = str(matriz[i][j])+","
#                 archivo.writelines(dato_a_escribir)

#Versión de Ulises
def guardar_archivo_CSV(matriz:list,ruta:str):
    with open(ruta,"w") as archivo:
        for fila in matriz:
            archivo.write(str(fila).strip("[").strip("]"))
            archivo.write("\n")
            #archivo.write(str(fila).strip("[").strip("]")+"\n") -> En una sola línea

guardar_archivo_CSV(mi_matriz, "Clase17/matriz.csv")