'''SCRABBLE:
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano. '''

# palabras = ['A5','B6','I7',....]

# Import
import random
import string

# Crear la lista con todas las letras y puntos (aleatorios)
puntos_letras = []
letra = ''

for letra in string.ascii_uppercase:
    puntos_letras.append(letra+str(random.randint(1,9)))

print(puntos_letras)

# Pedir al usuario ingresar la palabra [palabra_jugada]

while True:
    palabra_jugada = input('Ingresa la palabra jugada en mayúsculas ')
    if palabra_jugada.isalpha() == True:
        break
    else:
        print('Palabra ingresada incorrecta, vuelva a probar...')

# Calcular los puntos
puntos_totales = 0

for letra in palabra_jugada:                    # Recorer la plabara jugada letra por letra
    for letraA in string.ascii_uppercase:       # Comparar la letra anterior con el abecedario para saber la posición (letraA)
        if letra == letraA:
            # Utilizamos la posición (letraA) para buscar en la lista de puntos
            puntos_totales += int(puntos_letras[string.ascii_uppercase.index(letraA)][1])

print('Los puntos totales dada la palabra',palabra_jugada, puntos_totales)