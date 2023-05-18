'''ANALISIS DE DATOS CLIMÁTICOS 
Datos de clima = [Temperatura, Humedad , Presión atmosférica, Mes] en una ciudad durante un año. 
Resolver:   -Temperatura promedio de cada mes
            -Humedad promedio y la presión atmosférica promedio durante todo el año. 

Array de 3 columnas y n filas, 
n es el número de mediciones'''

# Tools :  mean()

import numpy as np
import random

###### GENERAR DATOS ALEATORIOS (no obligatorio) ######

# datos[n] = [temp, hum, pres, mes]      n filas = [mediciones]

# Función: Generar Temperatura random
def temp_rand():
    return random.randint(1,40)

# Función: Generar Humedad random
def hum_rand():
    return random.randint(10,90)

# Función: Generar Temperatura random
def pres_rand():
    return random.randint(1001,1012)

# Función: Generar Mes random
def mes_rand():
    return random.randint(1,12)

# Generar array de datos
# datos[n] = [temp, hum, pres, mes]      n filas = [mediciones]
n = random.randint(10,15)
datos = np.zeros([n, 4], int)

for num in np.arange(n):
    datos[num] = [temp_rand(), hum_rand(), pres_rand(), mes_rand()]

###### PROBLEMA A PARTIR DE ACÁ ######

## Temperatura promedio de cada mes
# Array de meses | temp_meses = [mes, mediciones, suma temperaturas del mes]
temp_meses = np.zeros((0,3), int)

for num in np.arange(n):
    mes = datos[num, 3]
    temp = datos[num, 0]

    # Si no está prensente el mes se agrega
    if mes not in temp_meses[:, 0]:
        temp_meses = np.append(temp_meses, [[mes, 1, temp]], axis=0)

    # Si está presente se le agrega la temperatura y +1 medición
    else:
        fila = np.where(temp_meses[:, 0] == mes) #(temp_meses[:, 0] == mes)
        print(fila)
        temp_meses[fila, 1] += 1
        temp_meses[fila, 2] += temp

# Inicializar
temp_meses_promedio = np.zeros((0,2), int)

# Se calcula el promedio por mes teniendo las mediciones y la catidad de mediciones
for nDato in np.arange(len(temp_meses)):
    promedio_mes = temp_meses[nDato, 2] / temp_meses[nDato, 1]
    temp_meses_promedio = np.append(temp_meses_promedio, [[temp_meses[nDato, 0], promedio_mes]], axis=0)


print('Los datos son [temp, hum, pres, mes]:\n', datos)
print('Las temperaturas promedio por mes son:\n', temp_meses_promedio)

## Humedad y Presión promedio del año
# Humedad promedio del año
print('La humedad promedio del año es:\n', datos[:,1].mean())

# Presión promedio del año
print('La presión promedio del año es:\n', datos[:,2].mean())