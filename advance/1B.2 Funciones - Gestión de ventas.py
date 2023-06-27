'''GESTIÓN DE VENTAS 
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una 
estructura de datos adecuada para almacenar la información de las ventas 
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para 
agregar el producto vendido con su precio y otro para mostrar las ventas de 
productos con sus respectivos precios.'''

## Ejercicio 2: Gestión de ventas ##

def agregar_prod_precio(prod_, precio_):
    prod_agregar = {"Producto": prod_, "Precio": precio_}
    lista_precios.append(prod_agregar)
    

def mostrar_ventas():
    for productos in lista_precios:
        print("Producto:", productos["Producto"])
        print("Precio:", productos["Precio"])
        print("---------")

lista_precios = []

# Ejemplos
agregar_prod_precio("Arroz", 3)
agregar_prod_precio("Pera", 1)
agregar_prod_precio("Banana", 2)

# Imprimir la lista
mostrar_ventas()