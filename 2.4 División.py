'''DIVISION:
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el 
divisor es cero el programa debe mostrar un error.'''

# Pedimos dos números
num1 = float(input('Escribe el primer número '))
num2 = float(input('Escribe el segundo número '))

# Mostramos por pantalla la división

if num2 == 0:
    print('La división sobre cero no es posible')
else:
    print('El resultado de la división de', num1, 'sobre',num2,'es',num1/num2)
