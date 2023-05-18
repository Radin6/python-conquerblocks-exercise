'''EL COMERCIAL:
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:
Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9 : 4 unidades
Los precios de cada uno de estos productos son como siguen:
Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
la cantidad total de ventas, el dinero facturado por producto y el dinero total'''

# Unidades totales vendidas (uni_total_vend), Dinero facturado por producto , Dinero total (eur_total)

# Import
import re

# Textos con información dada
precios_prod_texto = '''Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU'''

uni_vend_texto = '''Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9: 4 unidades'''

## Transformar texto de precios por productos a una lista de listas según:
## [['Producto 1', precio1],['Producto 2', precio2], ...] 
precios_prod = re.split('\n|\t \t',precios_prod_texto)          # Formo la lista cortando texto en '\n' or '\t \t'
precios_prod = [linea.lstrip() for linea in precios_prod]       # Elimino espacios de la iquierda
precios_prod = [linea.rstrip(' EU') for linea in precios_prod]  # Elimino ' ER' de la derecha
precios_prod = [linea.split(': ') for linea in precios_prod]    # Creo una lista de listas, separando en ': '

# Transformar todos los números o sea columna 2 (1) a números enteros | prod = producto
precios_prod = [[precios_prod[prod][0],float(precios_prod[prod][1])] for prod in range(len(precios_prod))]

## Transformar texto de unidades vendidas por producto a una lista de listas según:
## [['Producto 1', uniades1],['Producto 2', unidades2], ...] 
uni_vend = re.split('\n|\t \t',uni_vend_texto)                  # Formo la lista cortando texto en '\n' or '\t \t'
uni_vend = [linea.rstrip(' unidades') for linea in uni_vend]    # Elimino ' unidades' de la derecha
uni_vend = [linea.split(': ') for linea in uni_vend]            # Creo una lista de listas, separando en ': '

# Transformar todos los números o sea columna 2 (1) a números enteros 
uni_vend = [[uni_vend[prod][0],int(uni_vend[prod][1])] for prod in range(len(uni_vend))]

# Imprimir las Unidades totales vendidas
uni_total_vend = 0
prod = 0    # producto
for prod in range(len(uni_vend)):
    uni_total_vend += uni_vend[prod][1]

print('Las unidades totales vendidas son:', uni_total_vend)

# Imprimir Dinero facturado por producto y Dinero total (eur_total)
eur_total = 0

print() # un espacio = \n
for prod_L1 in range(len(uni_vend)):                            # Voy pasando por la lista de productos vendidos
    for prod_L2 in range(len(precios_prod)):                    # Voy pasando por la lista de todos los productos
        if uni_vend[prod_L1][0] == precios_prod[prod_L2][0]:    # Cuando estos coinciden se calcula: precio de la unidad x unidad
            print('Con el', uni_vend[prod_L1][0], 'se facturó un total de',uni_vend[prod_L1][1]*precios_prod[prod_L2][1])
            # Se aprovecha el loop para calcular el total facturado
            #Cant total  precio de la unidad x unidad
            eur_total += uni_vend[prod_L1][1]*precios_prod[prod_L2][1]  

print('\nEl dinero total facturado es:', eur_total, 'euros')