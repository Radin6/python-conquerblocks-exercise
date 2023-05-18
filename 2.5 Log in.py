'''LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). 
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe 
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la 
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)'''

# Establecemos la contraseña
contra = 'Radio13='

# Pedimos al usuario que introduzca la contraseña
contraU = input('Introduce la contraseña ')

# Verificamos si la contraseña es correcta
if contra == contraU:
    print('La contraseña ingresada es correcta, ingresando al sistema ')
else:
    print('La contraseña ingresada es incorrecta, tiene un intento más')
    contraU = input('Introduce la contraseña ')
    if contra == contraU:
        print('La contraseña ingresada es correcta, ingresando al sistema ')
    else:
         print('La contraseña ingresada es incorrecta, se ha bloqueado su acceso')