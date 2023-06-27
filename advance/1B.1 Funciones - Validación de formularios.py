## Ejercicio 1 : Validación de formularios ##
'''Requisitos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 
caracteres
3. Que el email contenga un “@“ y un “.”'''

def validar_formulario(nombre_, email_, tel_):
    valido = True

    if len(nombre_) < 3:
        valido = False

    if not tel_.isnumeric():
        valido = False
   
    if "@" not in email_ or "." not in email_:
        valido = False

    if valido:
        return print('El registro es válido')
    else:
        return print('El registro NO es válido')

# Ingresar datos
nombre = input('Introduce el nombre\n')
email = input('Introduce el email\n')
tel = input('Introduce el número de teléfono\n')

validar_formulario(nombre, email, tel)