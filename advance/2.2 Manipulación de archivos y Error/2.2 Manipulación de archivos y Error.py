'''MANIPULACION DE ARCHIVOS Y FILENOTFOUNDERROR 
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de 
gatos en el primer archivo y tres nombres de perros en el segundo archivo. 
Escribe un programa que intente leer estos archivos e imprima el contenido 
de cada archivo en la pantalla. Envuelve tu código en un bloque try-except 
para capturar el error de FileNotFoundError, e imprime un mensaje amigable 
si falta algún archivo. Mueve uno de los archivos a una ubicación diferente 
en tu sistema y asegúrate de que el código en el bloque except se ejecute 
correctamente. Modifica tu bloque except para que falle en silencio si falta 
alguno de los archivos.'''

archivo1 = "cats.txt"
archivo2 = "dogs.txt"

try:
    archivo_open = archivo1

    with open(archivo_open) as archivo:
        contenido1 = archivo.read()

    archivo_open = archivo2

    with open(archivo_open) as archivo:
        contenido2 = archivo.read()

except FileNotFoundError:
    print("ERROR: No se encuentra el archivo:", archivo_open)

else:
    print(f"El archivo {archivo1} contiene:\n", contenido1)
    print(f"El archivo {archivo2} contiene:\n", contenido2)

## Modificado: Falla en silencio ##
print("\n2 - Falla en silencio\n")

try:
    with open(archivo_open) as archivo:
        contenido = archivo.read()

except FileNotFoundError:
    None
else:
    print(f"El archivo {archivo1} contiene:\n", contenido)

try:
    with open(archivo2) as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    pass
else:
    print(f"El archivo {archivo2} contiene:\n", contenido)



    


    