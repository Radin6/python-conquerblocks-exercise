'''EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla.'''

# Pedir cuatro números
num1 = int(input('Escriba el primer número '))
num2 = int(input('Escriba el segundo número '))
num3 = int(input('Escriba el tercer número '))
num4 = int(input('Escriba el cuarto número '))

# If statement para calcular el mayor
if num1>num2 and num1>num3 and num1>num4:
    print('El primer número',num1,'es el mayor')
elif num2>num3 and num2>num4:
    print('El segundo número',num2,'es el mayor')
elif num3>num4:
    print('El tercer número',num3,'es el mayor')
elif num4>num3:
    print('El cuarto número',num4,'es el mayor')
else:
    print('Ocurrió un error en el ingreso de los números')

