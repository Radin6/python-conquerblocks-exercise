'''MATRIZ:
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos) '''
import random

# Función para crear un array con 3 items por fila y de 1 a 4 (azar) filas.
def azar():
    a=[[]]

    filas = random.randint(1,4)
    columnas = 3

    for i in range(filas-1):
        a.append([])

    for i in range(filas):
        #print("Enter elements for row ",i+1)
        for j in range(columnas):
            num = random.randint(1,9)
            a[i].append(num)
    return a
# Fin Función

lista_suma_fila = []
array = False
M = azar()
print(M)

# 1. La fila cuyos elementos suman el máximo
if len(M) >= 2: # Siendo mayor o igual a 2 es un array

    array = True    # Lo utilizo en el inciso 2
    print('M es una array')

    # Creo una lista con la suma de las filas
    for i in range(len(M)):     
        lista_suma_fila.append(sum(M[i]))
    fila_max = lista_suma_fila.index(max(lista_suma_fila))
    print('\nLa fila con la suma mayor es la:', fila_max+1)
    #
else:   
    print('M es una lista')

print('La lista de la suma de las filas:', lista_suma_fila)

# 2. La columna cuyos elementos suman el máximo
lista_suma_columna = []

if array == True: # Si es True es un array, si es False es Lista
    # Creo una lista con la suma de las columnas
    for j in range(len(M[0])):
        suma_col = 0
        # Para cada columna 'j' voy sumando el valor de la fila 'i'
        for i in range(len(M)):
            suma_col = suma_col + M[i][j] 
        lista_suma_columna.append(suma_col)
    columna_max = lista_suma_columna.index(max(lista_suma_columna))
    print('\nLa columna con la suma mayor es la:', columna_max+1)

print('La lista de la suma de las columnas:', lista_suma_columna)