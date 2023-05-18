'''RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos.'''

# Pedir tres números
num1 = int(input('Escriba el primer número '))
num2 = int(input('Escriba el segundo número '))
num3 = int(input('Escriba el tercer número '))

# Comrpobar que sean 3 números diferentes
if num1 != num2 and num2 != num3 and num1 != num3:
    # Calculamos si la suma de 2 es igual a uno de los números
    if num1 == num2 + num3:
        print('El primer número', num1,'es igual a la suma del segundo',num2, 'y tercer número', num3)
    elif num2 == num1 + num3:
        print('El segundo número', num2,'es igual a la suma del primer',num1, 'y tercer número', num3)
    elif num3 == num1 + num2:
        print('El tercer número', num2,'es igual a la suma del primer',num1, 'y segundo número', num2)
    else:
        print('Nigún número es igual a al suma de los otros dos números')
else:
    print('Alguno de los números que introdujo son iguales')