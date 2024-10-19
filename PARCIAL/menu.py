from funciones import *   

salir = "N"
menu = '''

    A) Ingresar numero
    B) Generar lista de mayúsculas
    C) Mostrar lista
    D) Ingresar letra mayúscula
    E) Ingresar cadena "ASC" o "DESC"
    F) Ingresar dos numeros enteros
    G) Generar matriz aleatoria
    H) Mostrar matriz
    I) Salir

'''

bandera_A = False
bandera_B = False
bandera_F = False
bandera_G = False
matriz_cargada = []

while salir == "N":
    opciones = input(menu)
    match opciones:
        case "A":
            bandera_A = False
            numero_ingresado = None
            while bandera_A == False:
                numero_ingresado = solicitar_numero_entero("\nIngre un número numero: ", "\nERROR: Ingrese un número entre 3-15: ",  3, 15)
                bandera_A = True
                print("\nNúmero ingresado correctamente.")  

        case "B":
                if bandera_A == False:
                    print("\nERROR: ¡Primero debe ingresar un número en la opción A!")
                else: 
                    lista_de_mayusculas = generar_lista_aleatoria_mayusculas(numero_ingresado)
                    bandera_B = True
                    print("\nLista de mayúsculas generada correctamente.")  

        case "C":
            if bandera_B == False:
                print("\nERROR: ¡Primero debe generar la lista en la opción B!")
            else:
                print(f"\nLista de mayúsculas:\n")
                mostrar_lista(lista_de_mayusculas)

        case "D":
            if bandera_B == False:
                print("\nERROR: ¡Primero debe generar la lista en la opción B!")
            else:
                letra_mayuscula = solicitar_mayuscula("\nIngrese una letra mayúscula: ")
                if buscar_dato(lista_de_mayusculas, letra_mayuscula) == False:
                    print(f"\nLa letra {letra_mayuscula} no se encuentra en la lista.")
                else:
                     posiciones = buscar_indices_dato(lista_de_mayusculas, letra_mayuscula)
                     if len(posiciones) == 1:
                         print(f"\nLa letra {letra_mayuscula} se encuentra en el índice: {posiciones}")
                     else:    
                         print(f"\nLa letra {letra_mayuscula} se encuentra en los índices: {posiciones}")
        case "E":
            if bandera_B == False:
                print("\nERROR: ¡Primero debe generar la lista en la opción B! ")
            else:
                ordenar_y_mostrar_copia_de_lista_en_orden(lista_de_mayusculas,"Ingrese ASC o DESC: ")

        case "F":
            cant_filas = solicitar_numero_entero("\nIngresar la cantidad de filas: ", "\nError: Ingrese un numero entre 3-10: ",  3, 10)
            cant_columnas = solicitar_numero_entero("\nIngresar la cantidad de columnas: ", "\nError: Ingrese un numero entre 3-10: ",  3, 10) 
            bandera_F = True 

        case "G":
             if bandera_F == False:
                print("\nERROR: ¡Primero debe ingresar la cantidad de filas y columnas en la opción F!")
             else:            
                matriz_creada = crear_matriz(cant_filas, cant_columnas, 0)
                cargar_matriz_num_aleatorios(matriz_creada)
                print(f"\nMatriz aleatoria de orden {cant_filas}x{cant_columnas} generada.")
                bandera_G = True

        case "H":
             if bandera_G == False:
                print("\nERROR: ¡Primero debe generar la matriz en la opción G!")
             else:
                print(f"\nMatriz {cant_filas}x{cant_columnas}:\n")
                mostrar_matriz(matriz_creada)

        case "I":
            salir = input("\nDesea salir y terminar el programa? S/N: ")
            
        case _ : 
            print("\nPor favor, ingrese una opción válida: ")   