'''MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula'''

# Pedir introducir letra
letra = str(input('Introduce una letra '))

# Resolver
if letra == letra.lower():
    print('La letra está en minúscula')
elif letra == letra.upper():
    print('La letra está en mayúscula')
else:
    print('Hay algún error en la letra ingresada')