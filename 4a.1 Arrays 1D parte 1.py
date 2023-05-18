'''ARRAYS 1D PARTE 1:'''

import numpy as np

# 1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
array_1 = np.zeros(8)
print('1.', array_1)

# 2. Haz que todos los elementos de este array sean igual a 2
array_1.fill(2)
array_1[:] = 2

print('2.', array_1)

# 3. Crea un array_2 que contenga todos los números pares del 1 al 10.
array_2 = np.arange(2,11,2)
print('3.', array_2)

# 4. Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados
suma = 0
for n in array_2:
    suma += n

print('4.1',suma)
print('4.2',array_2.sum())

# 5. Revierte array_2 y guárdalo en una variable independiente.
array_2_rev = array_2[::-1]
print('5.', array_2_rev)

# 6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido
# (Pista: Investiga el uso de intersect1d() de numpy)
print('6.1 Elementos comunes de array_1 y array_2:',np.intersect1d(array_1, array_2))
print('6.2 Elementos comunes de array_2 y array_2_rev:',np.intersect1d(array_2, array_2_rev))

# 7. Crea un arrays lleno de 1s con una longitud dada por el usuario
long = int(input('Ingrese una longitud '))
print(np.ones(long))