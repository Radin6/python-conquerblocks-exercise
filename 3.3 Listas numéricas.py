# LISTAS NUMERICAS:
# 1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].

numeros = []

for i in range(1,11):
    numeros.append(i)

# 2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
num_par_inv = []

for i in numeros[::-1]:
    if i%2 == 0:
        num_par_inv.append(i)

# 3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola.
for i in numeros:
    print('El cuadrado de', i,'es', i**2)

# 4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de compresión).
    
    #2 no entiendo como se haría

    #3
num_cuadrado = [i**2 for i in range(1,11)]

# 5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
min(numeros)

# 6. Haz lo mismo con el número más alto
max(numeros)

#7. Suma todos los elementos de la lista con y sin un bucle.
suma = 0

for i in numeros:
    suma = suma + i

sum(numeros)

# 8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras el punto 2.
print(numeros.index(8))
print(num_par_inv.index(8))
