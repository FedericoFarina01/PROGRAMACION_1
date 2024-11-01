'''
Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y
segundo examen parcial).
'''
def menu():
    menu = '''
1) Cargar datos
2) Mostrar datos
0) Salir del programa

Ingrese una opcion: 
'''
    respuesta = "n"
    lista_de_alumnos = []

    while respuesta == "n":
        seleccionar_opcion = input(menu)

        match seleccionar_opcion:
            case "1":
                alumno = cargar_datos("nombre", "nota_1", "nota_2")
                lista_de_alumnos.append(alumno)
            case "2":
                mostrar_lista_alumnos(lista_de_alumnos)
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "10":
                pass
            case "0":
                print("Cerrando programa")
                break
            case _:
                print("Opcion no valida, ingres un numero del 1 al 10")



def validar_rango(numero: str, minimo: int, maximo: int)-> bool:
    '''
    
    '''
    numero_valido = False

    if numero.isdigit() == True:
        if int(numero) >= minimo and int(numero) <= maximo:
            numero_valido = True

    return numero_valido
    
def cargar_datos(clave_nombre: str, calificacion_1:str, calificacion_2:str) -> dict:
    '''
    
    '''
    nombre_ingresado = input(f"Ingrese el {clave_nombre} del alumno: ")
    
    califiacion_1_ingresada = input(f"Ingrese la {calificacion_1} del alumno: ")
    while validar_rango(califiacion_1_ingresada, 1, 10) == False:
        califiacion_1_ingresada = input(f"Ingrese la {calificacion_1} del alumno: ")
    califiacion_1_ingresada = int(califiacion_1_ingresada)

    califiacion_2_ingresada = input(f"Ingrese la {calificacion_2} del alumno: ")
    while validar_rango(califiacion_2_ingresada, 1, 10) == False:
        califiacion_2_ingresada = input(f"Ingrese la {calificacion_2} del alumno: ")
    califiacion_2_ingresada = int(califiacion_2_ingresada)

    alumno = {clave_nombre: nombre_ingresado, calificacion_1: califiacion_1_ingresada, calificacion_2: califiacion_2_ingresada}

    return alumno


"""
2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
donde cada fila representa un alumno y cada columna representa uno de sus datos.
"""

def mostrar_lista_alumnos(lista_alumnos: list) -> None:
    """
    """
    print("Nombre Nota1 Nota2")
    for i in range(len(lista_alumnos)):
        un_alumno = lista_alumnos[i]
        print(un_alumno["nombre"], un_alumno["nota_1"], un_alumno["nota_2"])


menu()