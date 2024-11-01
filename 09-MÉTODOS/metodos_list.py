#1) Agregar 3 nombres de alumnos (ingresados por el usuario) al final de la lista.

lista_alumnos = []

def agregar_alumnos(cant_alumnos:int, lista:list, mensaje:str) -> None :
    '''
    '''
    for _ in range (cant_alumnos):
        nombre_alumno = input(mensaje)
        lista.append(nombre_alumno)



def mostrar_lista(lista:list) -> None:
    '''
    '''
    for i in range(len(lista)):
        print(lista[i])


def agregar_nombre(lista:list, indice:int, mensaje:str) -> None:
    '''
    '''
    nombre_alumno = input(mensaje)
    lista.insert(indice,nombre_alumno)




agregar_alumnos(3,lista_alumnos, "Ingresa el nombre del alumno: ")
mostrar_lista(lista_alumnos)

#2) Insertar un 4to nombre de alumno (ingresado por el usuario) al principio de la lista.

agregar_nombre(lista_alumnos,0,"Ingresa el nombre del alumno: ")


# 3) Extender la lista agregando 2 nombres adicionales al principio de la misma.
print("Extiende con dos nombres")
lista_alumnos2 = []
agregar_alumnos(2, lista_alumnos2, "Ingresa un alumno: ")
lista_alumnos2.extend(lista_alumnos)
mostrar_lista(lista_alumnos2)

# 4) Contar e informar cuántas veces aparece un nombre ingresado por el usuario
print("Informa la cantidad")
nombre_a_buscar = input("Ingrese nombre a buscar: ")
cantidad = lista_alumnos2.count(nombre_a_buscar)
print(f"Se encontraron {cantidad} alumnos llamados {nombre_a_buscar}")

# 5) Eliminar de la lista un nombre ingresado por el usuario
print("Elimina un nombre")
nombre_a_eliminar = input("Ingrese el nombre a eliminar: ")
lista_alumnos2.remove(nombre_a_eliminar)
mostrar_lista(lista_alumnos2)

# 6) Eliminar el penúltimo nombre de la lista e informar que nombre se eliminó
print("Elimina el penultimo nombre: ")
nombre_eliminado = lista_alumnos2.pop(-2)
# nombre_eliminado = lista_alumnos2.pop(len(lista) - 1)
print(f"Se elimino a {nombre_eliminado}")
mostrar_lista(lista_alumnos2)

# 7) Ingresar un nombre por consola, buscarlo e informar su índice.

print("Nombre a buscar el indice")
nombre_a_buscar = input("Ingrese el nombre a buscar: ")
indice_buscado = lista_alumnos2.index(nombre_a_buscar)
print(f"El nombre {nombre_a_buscar} se encuentra en el indice {indice_buscado}")
mostrar_lista(lista_alumnos2)

# 8) Ordenar los nombres descendentemente.
lista_alumnos2.sort(reverse=True)
print("Se ordeno descendentemente")
mostrar_lista(lista_alumnos2)

# 9) Crear una copia de la lista.
copia_lista_alumnos = lista_alumnos2.copy()
print("Creo una copia de la lista")
mostrar_lista(lista_alumnos2)
mostrar_lista(copia_lista_alumnos)

# 10) Limpiar la lista original eliminando todos sus elementos, mostrar la lista original y la copia.
print("Limpiando la lista original")
lista_alumnos2.clear()
mostrar_lista(lista_alumnos2)
mostrar_lista(copia_lista_alumnos)