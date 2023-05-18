'''ARRAYS 1D PARTE 2:'''

import numpy as np

# 1. Crea un array con 15 números enteros aleatorios entre 1 y 100
arr1 = np.random.randint(1,100, size=15)
print('1.', arr1)

# 2. Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados
prod = 1
for n in arr1.view():
    prod *= n

print('2.1', prod)
print('2.2', arr1.prod())

# 3. Crea otro array con 10 números decimales aleatorios entre 0 y 1
arr2 = np.random.uniform(0,1, size=10)

print('3.',arr2)

# 4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

min_len = min(len(arr1), len(arr2))
arr3 = arr1[:min_len] + arr2[:min_len]
print('4.1', arr3)
print('4.2', np.add(arr1[:min_len], arr2[:min_len]))

# 5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)
arr3 = arr1[:min_len] - arr2[:min_len]
print('5.1', arr3)
print('5.2', np.subtract(arr1[:min_len], arr2[:min_len]))

# 6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)
arr3 = arr1[:min_len] * arr2[:min_len]
print('6.1', arr3)
print('6.2', np.multiply(arr1[:min_len], arr2[:min_len]))

# 7. Encuentra el valor más alto del primer array que has creado.
print('7.', arr1.max())

# 8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard deviation) de los arrays 
# (Nota: No nos importa el significado matemático de estos valores, 
# lo importante es que encuentres que función de numpy necesitas. 
# Puedes hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele haber más resultados)

print('8.1','Media arr1:' , arr1.mean(), '| Media arr2:' , arr2.mean())
print('8.2','Median arr1:' , np.median(arr1) , '| Median arr2:' , np.median(arr2))
print('8.3', 'Standard deviation arr1:', np.std(arr1), 'Standard deviation arr2:', np.std(arr2))