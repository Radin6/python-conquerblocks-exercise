# PILLANDO SOLTURA:
# 1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
# añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
# elementos únicos.

    # Lista ejemplo
lista = [5,7,3,6,8,3,7,9,1,2]
    # Copiamos la lista
listaC = lista[:]

    # Buscamos elementos similares para borrarlos de la listaC
for i in lista:
    n = 0
    for x in lista:
        if i == x:
            n = n + 1
    if n >= 2:
        listaC.remove(i)

print(lista)
print(listaC)

#2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.
lista1 = [1,2,7,9]
lista2 = [4,6,8,3]
listaF = lista1 + lista2
listaF = listaF.sort()

#3. Escribe un script que encuentre el segundo número más grande de una lista.
lista3 = lista[:]
print(lista3)
    # Lo ordeno en ordeno en orden descendente, 
lista3.sort(reverse=True)
    # Borro el/los máximo/s
lista3.remove(lista3[0])
print(lista3)
    # Ya el máximo borrado, me quedaría el segundo máximo primero
print('El segundo número mayor es', lista3[0])


#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).
num = int(input('Escribe un número '))
n = 0

for i in lista:
    if num < i:
        n = n + 1

print('Hay',n , 'elementos más grandes que', num)

#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este.

num = int(input('Escribe un número '))
n = 0

for i in lista:
    if i%num ==0:
        n = n + i

print('El resultado de la suma de los número divisibles por',num,'es', n)

#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.
num = int(input('Escribe un número '))
lista6 = []

for i in lista:
    if i < num:
        lista6.append(i)
n_max = max(lista6)

print('El número más alto por debajo de',num,'es', n_max)
#7. Crea un script que extraiga los elementos comunes entre dos listas.

lista1 = []
lista2 = []
lista_comun = []
    # Busco los números en común y formo una lista
for i in lista1:
    for x in lista2:
        if i == x:
            lista_comun.append(i)
    # Remuevo los números en común de la lista1 y lista2
for i in lista_comun:
    lista1.remove(i)
    lista2.remove(i)

#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)
num = input('Elige el número que quieres ver cuantas veces se repite')
n = 0

for i in lista:
    if num == i:
        n = n + 1

print('El número', num ,'se encuentra', n, 'veces')

#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.
lista_positivos = []

for i in lista:
    if i > 0:
        lista_positivos.append(i)

#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.
lista_string = ['hola','crypto','btc', 'hash']
lista_long = [len(i) for i in lista_string]

print(lista_long)

#11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en mayúscula. 
i = 0
lista_mayus = [i.upper() for i in lista_string]

print(lista_mayus)