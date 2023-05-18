'''PAR O IMPAR: 
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa 
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)'''

# Pedimos el número y la potencia a la cual elevarlo
num = int(input('Introduce el número '))
pot = int(input('Introduce la potencia '))
resultado = num**pot

# Damos el resultado de ese número a la potencia
print('Si elevamos',num , 'a la potencia',pot , 'obtenemos', resultado)

# Comprobamos si el número es par o impar
if resultado%2 == 0:
    print('El numero elevado a la potencia es par')
else:
    print('El número es impar')