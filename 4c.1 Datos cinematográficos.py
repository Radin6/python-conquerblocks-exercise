#DATOS CINEMATOGRÁFICOS

# películas[] = [título, género, duración, año, calificación]
# Resolver: -Género más popular (gen_popular), 
# -películas por década (peli_decada)
# -duración promedio de cada género (dura_genero)

import numpy as np

peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

## Género más popular (gen_popular)

# Array con los géneros tal cual peliculas[]
generos = np.array([pelicula[1] for pelicula in peliculas])

# Array con los géneros únicos y el número de veces que aparece
generos_unicos, conteos = np.unique(peliculas[:,1], return_counts=True)

# Array con los índices con mayor conteo en forma descendente
conteos_desc = np.argsort(conteos)[::-1]

genero_popular = generos_unicos[conteos_desc[0]]

print('El género más popular es:', genero_popular)

##  Películas por década (peli_decada)
print('-------------------------------------------------')
# Array de años según posición en array películas
años = np.array(peliculas[:,3])

#  Array con las décadas según posición en array películas
decadas = np.array([año[0:3]+'0' for año in años])

# Array con las décadas sin repetir
decadas_unicas = np.unique(decadas)

for decada in decadas_unicas:
    decada_filtrada = peliculas[decadas == decada]
    decada_filtrada = decada_filtrada[:,0]
    print(f'Para la década {decada}, se estrenaron {decada_filtrada}')

## Duración promedio de cada género (dura_genero)
print('-------------------------------------------------')

# Array con géneros únicos
generos_unicos = np.unique(generos)

for genero in generos_unicos:
    genero_filtrado = peliculas[generos == genero]
                #  duración del genero filtrado.
    genero_media = np.mean(genero_filtrado[:,2].astype('float16'))
    print(f'Para el género {genero}, el promedio de duración es {genero_media}')