'''BUCLES:
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
*
2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última.
4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.'''

# Pedir num entero
num = int(input('Escribe un número entero '))

# 1.
for i in range(1,num+1):
    print('*'*i)
for i in range(1,num+1):
    print('*'*(num-i))

# 2.
contra = '#68M='
contraI = input('Ingrese la contraseña ')

while contraI != contra:
    print('La contraseña ingresada es incorrecta, vuelva a ingresarla')
    contraI = input()
print('La contraseña ingresada es CORRECTA, ingresando...')

# 3.
palabra = input('Ingrese una palabra ')

palabraR = palabra[::-1]

for i in palabraR:
    print(i)

# 4.
frase = input('Ingrese una frase ')
letra = input('Ingrese una letra ')
n = 0

for i in frase:
    if letra == i:
        n = n + 1

print('La letra:', letra, 'se encuentra:', n, 'veces en la frase:', frase)

