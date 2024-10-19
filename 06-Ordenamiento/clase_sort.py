""" lista = [6, 3, 4, 5, 1, 2, 5, -2, 9]

print(lista) #PROHIBIDO

# ordenamos Asc
for i in range(len(lista) -1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            #Swap
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux

print(lista) #PROHIBIDO """


#--------------------------------------

apellidos =         ["Perez", "Fernandez", "Gomez"] #3
antiguedades =      [  15,        5,          20  ] #3
legajos =           [  435,      250,         673 ] #3
codigo_sector_emp = [   1,         2,          1  ] #3

id_sectores = [    1,         2  ] #2
sectores =    ["Sistemas", "RRHH"]

print(f"{"Apellido":15}{"Antiguedad":12}{"Legajo":8}{"Sector":4}")
print("--------------------------------")
for i in range(len(apellidos)):  #3
    for j in range(len(sectores)):  #2
        # 1, 2, 1 == 1, 2
        if codigo_sector_emp[i] == id_sectores[j]:
            print((f"{apellidos[i]:10}{antiguedades[i]:12}{legajos[i]:9}{sectores[i]:8}"))