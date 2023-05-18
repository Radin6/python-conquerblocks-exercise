# ANALISIS DE DATOS - VENTAS POR MES

import numpy as np
import random

###### GENERAR DATOS ALEATORIOS (no obligatorio) ######

# Lista de categorías
catego = ['ropa', 'alimentos', 'electrodomésticos', 'muebles']

# Función: da una Categoría al azar
def catego_random():
    return random.choice(catego)

# Función: da una fecha al azar
def random_fecha():
    dia = str(random.randint(1,30))
    if len(dia) == 1:
        dia = '0'+ dia
    mes = str(random.randint(1,12))
    if len(mes) == 1:
        mes = '0'+ mes
    año = '2022'
    
    fecha = año + '/' + mes + '/' + dia

    return fecha

# Función: da un monto al azar
def monto_random():
    return str(random.randint(1,50))

# Número de ventas al azar
n = random.randint(7,12)


###### PROBLEMA A PARTIR DE ACÁ ######

# ventas[n] = [fecha, monto, categoría]
ventas = np.zeros([n, 3], dtype='U100')

for venta in range(n):
    #print(random_fecha(), monto_random(), catego_random())
    ventas[venta] = [random_fecha(), monto_random(), catego_random()]

# ventas = ventas[:,1].astype(int) 
print(ventas)

## Calcular ventas por meses : meses = [[mes1, ventas1],[mes2, ventas2],...]

# Inicalizar un array numpy vacío
meses = np.empty((0,2), int)

# recorro las ventas una a una
for n in np.arange(len(ventas)):
    mes = int(ventas[n,0][5:7])
    nro_ventas = int(ventas[n,1])

    # Agregar si el més no se encuenta en la lista
    if mes not in meses:
        meses = np.append(meses, [[mes, nro_ventas]], axis=0)

    # Si ya se encuentra sumar/añadir el número de ventas
    else:
        fila = np.where(meses[:,0] == mes)
        meses[fila, 1] += nro_ventas

print('[Mes , Ventas del mes]\n', meses)

## Calcular venta por categoría
# Array de categorías
catego = ['ropa', 'alimentos', 'electrodomésticos', 'muebles']

# Inicalizar un array numpy vacío
ventas_catego = np.empty((0,2), dtype='U100')

# Generar un array de categorías e inicializar a 0
for tipo in catego:
    ventas_catego = np.append(ventas_catego ,[[tipo,'0']], axis=0)

# recorro las ventas una a una
for n in np.arange(len(ventas)):
    tipo = str(ventas[n,2])
    nro_ventas = str(ventas[n,1])

    # Buscar la fila donde está esa categoría, y añadir las ventas a esa categoría
    fila = np.where(ventas_catego[:,0] == tipo)
    venta = ventas_catego[fila, 1]
    ventas_catego[fila, 1] = str(int(ventas_catego[fila, 1]) + int(nro_ventas))

print('[Categoría , Ventas del la categoría]\n', ventas_catego)