import json
import os

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, "r") as archivo:
        return json.load(archivo)

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)