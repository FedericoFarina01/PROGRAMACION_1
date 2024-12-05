import json 
import os

def leer_json(nombre_archivo:str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            lista_puntajes = json.load(archivo)
    else:
        lista_puntajes = []
        
    return lista_puntajes

def guardar_json(nombre_archivo:str,lista_puntajes):
    with open(nombre_archivo,"w"):
        json.dump(lista_puntajes,indent=4)
    
