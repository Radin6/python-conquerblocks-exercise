# # EMPRESA DE ELECTRONICA

import numpy as np

datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                ['2022-01-15', 'Componente 1', 'Lote B', 90],
                ['2022-02-01', 'Componente 2', 'Lote C', 85],
                ['2022-01-15', 'Componente 2', 'Lote D', 95],
                ['2022-03-01', 'Componente 1', 'Lote E', 75],
                ['2022-03-15', 'Componente 2', 'Lote F', 90],])

# datos = [fecha], [tipo], [lote], [calidad (0-100)]

## 1. Tipo de componente con calidad más alta
comps = datos[:,1]
comps_unicos = np.unique(comps)
calidad = datos[:,3].astype(float)
promedios = np.zeros(len(comps_unicos))
i = 0

for comp in comps_unicos:
    calidad_comps = calidad[comps == comp]
    calidad_media = np.mean(calidad_comps)
    promedios[i] = calidad_media
    i += 1

comp_calidad_max = comps_unicos[np.argmax(promedios)]
print('El componente con la calidad mayor es:', comp_calidad_max)

## 2. Componenetes producidos por mes
print('-------------------------------------------------')
# Array de meses con igual posición a array datos
meses = np.array([mes[5:7] for mes in datos[:, 0]])

# Array de meses únicos
meses_unicos, counts = np.unique(meses, return_counts=True)

for i in range(len(meses_unicos)):
    print(f'En el mes {meses_unicos[i]} se produjeron {counts[i]} componentes')

## 3. Puntuación de calidad promedio por cada componente
# Ya está calculado en 1.
print('-------------------------------------------------')

for comp in comps_unicos:
    comp_filtrados = datos[comps == comp]
    comp_calidad_media = np.mean(comp_filtrados[:,3].astype('int8'))
    print(f'Para el componente {comp} la calidad promedio es {comp_calidad_media}')