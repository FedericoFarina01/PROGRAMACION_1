# 2)Desarrollar una funcion que reciba una cadena de caracteres, suprima los caracteres repetidos y devuelva la cadena resultante.
def quitar_repetido(cadena:str) -> str:
    """
    """
    # Hooola (Hola)
    acumulador = ""
    
    for i in range(len(cadena)-1):
        if cadena[i] != cadena[i+1]:
            acumulador += cadena[i]
    acumulador += cadena[len(cadena)-1]
    return acumulador
    
print(quitar_repetido("Hooolo"))