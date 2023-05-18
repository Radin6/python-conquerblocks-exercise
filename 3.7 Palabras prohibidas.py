'''PALABRAS PROHIBIDAS:
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida. '''


# Construir la lista de 5 palabras introducidas por el usuario
lista = [0,0,0,0,0]

for n in range(5):
    while True:
        lista[n] = input('Introduce una palabra: ').lower()
        if lista[n].isalpha() == True:
            break
        else:
            print('La palabra tiene carácteres incorrectos, intenta de nuevo...')

print('La lista es:', lista)

# Definir las 3 letras prohibidas
lista_no = [0,0,0]

for n in range(3):
    while True:
        lista_no[n] = input('Introduce una letra para prohibir: ').lower()
        if lista_no[n].isalpha() == True and len(lista_no[n]) == 1:
            break
        else:
            print('La letra no es de un solo caracter o tiene carácteres incorrectos, intenta de nuevo...')

print('Las letras prohibidas son:', lista_no)

# Filtrar las palabras de la lista original según si contiene o no las letras prohibídas
lista_filtrada = []
letra = ''

for palabra in lista:
        if lista_no[0] not in palabra and lista_no[1] not in palabra and lista_no[2] not in palabra:
            lista_filtrada.append(palabra)

print('Luego de filtrar la lista sería:', lista_filtrada)
