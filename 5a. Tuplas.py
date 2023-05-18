
# 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
print('Ejercicio 1')
mi_tupla = ('elemento1', 'elemento2', 'elemento3')
print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[2])

# 2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla.
# ¿Cuáles son las diferencias?
print('\nEjercicio 2')
mi_lista = ['elemento1', 'elemento2', 'elemento3']
mi_lista[0] = "A"
print(mi_lista)

mi_tupla = ('elemento1', 'elemento2', 'elemento3')
try:
    mi_tupla[0] = "B"
except:
    print("Las tuplas son Inmutables, no se pueden modificar sus elementos")

# 3. Crea una tupla de enteros y devuelve la suma de los elementos.
print('\nEjercicio 3')
mi_tupla = (1, 2, 3, 4)
print("La suma de mi tupla es:", sum(mi_tupla))

# 4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el
# primer caracter de cada string.
print('\nEjercicio 4')
mi_tupla = ('agua', 'queso', 'hoja')
mi_lista = list(mi_tupla)
mi_lista2 = []

for linea in mi_lista:
    mi_lista2.append(linea[0])

mi_tupla_iniciales = tuple(mi_lista2)
print(mi_tupla_iniciales)

# 5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares.
print('\nEjercicio 5')
mi_tupla = (1, 2, 3, 4, 5, 6)
prod = 1

for n in mi_tupla:
    if n%2 == 0:
        prod *= n

print('El producto de los números pares de mi tupla es:', prod)

# 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente.
print('\nEjercicio 6')
mi_tupla = (1, 2, 3, 4, 5, 6)

mi_tupla_reversed = tuple(sorted(mi_tupla, reverse=True))
print(mi_tupla_reversed)

# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).
print('\nEjercicio 7')
mi_tupla = (3, 2, 3, 4, 5, 4)
mi_set = set(mi_tupla)

print(mi_set)

# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el
# numero se encuentra en la tupla y falso en el caso contrario.
print('\nEjercicio 8')
mi_tupla = (1, 2, 3, 4, 5, 6)
input('Elije un número entero para saber si se encuentra en la cupla ')
print(n in mi_tupla)

# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
print('\nEjercicio 9')
mi_tupla1 = (1, 2, 3, 4)
mi_tupla2 = (5, 6, 7, 8)
mi_tupla_union = mi_tupla1 + mi_tupla2

print(mi_tupla_union)

# 10. Crea un script que dada una tupla de números devuelva el máximo y el mínimo.
print('\nEjercicio 10')
mi_tupla = (1, 2, 3, 4, 5, 6)

print('El máximo es: ', max(mi_tupla), '\nEl mínimo es: ', min(mi_tupla))

# 11. Crea un script que dada una tupla con strings devuelva el string más largo y el más
# corto. (Prueba añadiendo key=len a las funciones max y min).
print('\nEjercicio 11')
mi_tupla = ('azul', 'verde', 'naranja')

print('El string más largo es: ', max(mi_tupla, key=len), '\nEl string más corto es: ',min(mi_tupla, key=len))

# 12. Crea un script que dada una tupla devuelva el contenido en orden revertido.
print('\nEjercicio 12')
mi_tupla = ('hoja', 5, True)
mi_tupla_revertida = mi_tupla[::-1]

print(mi_tupla_revertida)

# 13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
# elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
# elementos de la tupla interna correspondiente.
print('\nEjercicio 13')
mi_tupla = ((1, 2), (3, 4), (5, 6))
mi_lista = []

for linea in list(mi_tupla):
    mi_lista.append(sum(linea))

print(tuple(mi_lista))