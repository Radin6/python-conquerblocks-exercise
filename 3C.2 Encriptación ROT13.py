# ENCRIPTACIÓN ROT13:
'''
1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
esta codificación ROT13 de la otra. '''

# Import
import random
import string

## 1 Generar string a traducir al azar
# Va a ser la longitud al azar del imput entre 5 y 15
azar = random.randint(5,10) 

# String con todos los caracteres posibles a introducir [a...z A...Z ÑñÇß]
abc = string.ascii_lowercase
ABC = string.ascii_uppercase
otros = 'ÑñÇß'

# Letras a seleccionar para la frase
letras = abc + ABC + otros   

frase_traducir = []

# Seleccionar letras al azar dentro de [letras] para formar [frase_traducir]
for num in range(azar):
    letra = letras[random.randint(0,len(letras)-1)]
    frase_traducir.append(letra)

print('Frase inicial:', frase_traducir)

## Generar un script para traducir
# Prefieron hacer una función a la cual le paso la frase an encriptar


def encriptar(frase_tradu):
    frase_final = []
    # Se calcula la longitud de abc (= longitud de ABC)
    max = len(abc) - 1

    for letra in frase_tradu:
        if letra in abc:
            indx = abc.index(letra)
            if indx+13 > max:
                indx = indx + 13 - max
            else:
                indx = indx + 13
            frase_final.append(abc[indx])
        elif letra in ABC:
            indx = ABC.index(letra)
            if indx+13 > max:
                indx = indx + 13 - max
            else:
                indx = indx + 13
            frase_final.append(ABC[indx])
        elif letra in otros:
            frase_final.append(letra)
    
    return frase_final

print('Frase final:', encriptar(frase_traducir))

## 2 Teniendo 2 cadenas decifrar si un es la encriptación ROT13 de la otra
print('----------------------------\n')

cadena1 = []    # Introducir una cadena para comprobar 
cadena2 = []    # Introducir una cadena para comprobar 

if cadena2 == encriptar(cadena1) and cadena1 != []:
    print('La candena 1:', cadena1, '\nes la encriptación ROR13 de la cadena 2\n', cadena1, '\n y viceversa')
else:
    print('Las cadenas NO están relacionadas')