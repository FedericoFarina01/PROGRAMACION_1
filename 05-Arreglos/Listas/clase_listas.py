def cargar_lista_secuencialmente(cantidad:int)->None:
    lista = [None] * cantidad
    for i in range (len(lista)):
        numero_ingresado = int(input("Ingrese un numero entero: "))
        while numero_ingresado < 0 or numero_ingresado > 10:
            numero_ingresado = int(input("Ingrese un numero entero: "))
        lista[i] = numero_ingresado
    return lista

numero_ingresado = int(input("Cuantos elementos desea cargar: "))
while numero_ingresado < 1 or numero_ingresado > 50:
    numero_ingresado = int(input("Cuantos elementos desea cargar: "))
mi_otra_lista = [] * numero_ingresado
mi_lista = cargar_lista_secuencialmente(numero_ingresado)
print(mi_lista)


def appen_casero(lista:list)->None:
   numero_ingresado = int(input("Cuantos elementos desea cargar: "))
   while numero_ingresado < 1 or numero_ingresado > 10:
         numero_ingresado = int(input("Cuantos elementos desea cargar: "))
   lista += [numero_ingresado]
   
mi_lista = [1, 2, 3]
print(mi_lista)
appen_casero(mi_lista)
print(mi_lista)



def cargar_lista_aleatoriamente(lista:list)->None:
    while True:

        #Indice
        indice_ingresado = int(input("Ingrese el indice a modificar: "))
        while indice_ingresado < 0 or indice_ingresado > (len(lista) - 1):
            indice_ingresado = int(input("Ingrese el indice a modificar: "))
        #Dato
        numero_ingresado = int(input("Ingrese una nota del 1 al 10 "))
        while numero_ingresado < 1 or numero_ingresado > 10:
            numero_ingresado = int(input("Ingrese una nota del 1 al 10 "))

        lista[indice_ingresado] = numero_ingresado

        respuesta = input("Desea seguir ingresando datos? S/N")
        if respuesta == "N":
            break


def buscar_indices_dato(lista:list, dato:int)->list:
    coincidencia = []
    for i in range(len(lista)):
        if dato == lista[i]:
            coincidencia += [i]
            break
    return coincidencia

lista = [1, 2, 3, 4]
print(lista)
coinc = buscar_indices_dato(lista, 3)
print(coinc)