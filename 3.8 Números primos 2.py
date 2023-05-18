'''NUMEROS PRIMOS 2:
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados '''
# Import
import random

# Crear una lista de tamaño variable de 10 a 20, con números enteros del 1 al 50
tam = 0 # Tamaño
lista_original = []

for tam in range(1,random.randint(10,20)):
    lista_original.append(random.randint(1,50))

print('Lista original:', lista_original)

# Crear una lista con los número primos
lista_primos = []

for num in lista_original:
    veces = 0
    for i in range(1,num+1):
        if i>1 and num % i == 0:
            veces += 1
    if veces == 1:
        lista_primos.append(num)

print('Lista de números primos:', lista_primos)

# Calcular cantidad total de números primos
num_total_primos = len(lista_primos)
print(num_total_primos)

# Calcular la suma total de los números primos
sum_total_primos = sum(lista_primos)
print(sum_total_primos)