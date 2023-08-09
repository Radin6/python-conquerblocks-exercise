import json

def grabar_favorito():
    
    favorito = input("Ingresa tu número favorito: ")
    filename = "text.json"

    with open(filename, "w") as archivo:
        json.dump(favorito, archivo)