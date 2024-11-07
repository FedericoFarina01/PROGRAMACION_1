from funciones import *

'''
Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y
segundo examen parcial).
'''
def menu():
    menu = '''
1) Cargar datos
2) Mostrar datos
3) Calcular promedio
4) Informar estado académico
5) Buscar alumno
6) Baja física
7) Baja Logica
0) Salir del programa

Ingrese una opcion: 
'''
    respuesta = "n"
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
            case "0":
                print("Cerrando programa")
                break
            case _:
                print("Opcion no valida, ingres un numero del 1 al 10")



