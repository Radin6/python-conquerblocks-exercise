'''ARRAYS 2D'''

import numpy as np

# 9. Crea un arrays lleno de 1s con una longitud dada por el usuario
long = int(input('Escribe una longitud '))
arr1 = np.ones(long, dtype=int)
print('9.', arr1)

# 10.Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
arr2 = arr1.reshape(3,-1)
print('10.', arr2)

# 11.Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
arr3 = arr2[:]

# 12.Concatena ambas estructuras horizontalmente y verticalmente
# (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)
print('12.')
print('Concatenate:\n', np.concatenate((arr2, arr3)))
print('Vstack:\n', np.vstack((arr2, arr3)))
print('Hstack:\n', np.hstack((arr2, arr3)))
