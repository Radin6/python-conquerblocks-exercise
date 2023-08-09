import json

filename = "text.json"

def decir_favorito():

    with open(filename) as archivo:
        contenido = json.load(archivo)

    return contenido