# 14.Crea un set y elimina uno de sus elementos.
print('\nEjercicio 14')
mi_set = {'perro', 'gato', 'ave'}

mi_set.discard('perro')
print(mi_set)

# 15.Crea un set vacío.
print('\nEjercicio 15')
mi_set_vacio = {}

print(mi_set_vacio)

# 16.Crea dos sets y encuentra su union, su intersección y su diferencia.
print('\nEjercicio 16')
mi_set1 = {1,2,3,6}
mi_set2 = {3,4,5,1}

print('Unión:', mi_set1 | mi_set2)
print('Intersección:', mi_set1 & mi_set2)
print('Diferencia:', mi_set1 - mi_set2)
print('Diferencia simétrica:', mi_set1 ^ mi_set2)

# 17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.
print('\nEjercicio 17')
mi_set1 = {1,2,3,6}
mi_set2 = {3,4,5,1}
mi_set_comun = mi_set1 & mi_set2

print(mi_set_comun)

# 18.Crea un script que dado un set con números devuelva el numero máximo y mínimo.
print('\nEjercicio 18')
mi_set1 = {1,2,3,6}
print('El máximo es: ', max(mi_set1), '\nEl mínimo es: ', min(mi_set1))

# 19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets.
print('\nEjercicio 19')
mi_set1 = {1,2,3,6}
mi_set2 = {3,4,5,1}
mi_set_unico = mi_set1 ^ mi_set2

print(mi_set_unico)

# 20.Crea un set con colores y comprueba si cierto color se encuentra en el set.
print('\nEjercicio 20')
mi_set = {'rojo', 'amarillo', 'azul', 'verde'}
color = input('Ingrese el color a verificar ')
print(color in mi_set)

# 21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en 
# el primer set pero no en el segundo.
print('\nEjercicio 21')
mi_set1 = {1,'rojo',3,6,'azul'}
mi_set2 = {3,'azul',4,5,'verde'}
mi_set3 = mi_set1 - mi_set2

print(mi_set3)

# 22.Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.
print('\nEjercicio 22')
mi_set = {1,3,6,5,9}
prod = 1

for n in list(mi_set):
    prod *= n

print(f'El producto de {mi_set} es {prod}')