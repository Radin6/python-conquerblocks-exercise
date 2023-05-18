'''CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla.'''

# Pide la contraseña
contra = input('Ingresa tu contraseña ')

# Verificamos si la contraseña tiene los carácteres requeridos

if ('a' in contra or 'e' in contra or 'i' in contra or 'o' in contra or 'u' in contra)\
     and '*' in contra and '#' in contra:
    print('Su Contraseña es SEGURA')
else:
    print('Su contraseña NO es segura')