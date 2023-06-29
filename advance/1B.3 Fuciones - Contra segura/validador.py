# Verificar requisitos:
# números y caracteres especiales
import string

def validar_contraseña(contra_):
    resultado = True
    lower = False
    upper = False
    numeric = False
    especial = False

    # Verificar si la longitud es al menos 4
    if len(contra_) < 4:
        print("ERROR: La ccontraseña tiene menos de 4 caracteres")
        resultado = False
        return resultado
    
    resultado = False

    for caracters in contra_:
        # Verificar si contiene al menos una letra minúscula
        if caracters.islower():
            lower = True

        # Verificar si contiene al menos una letra mayúscula
        if caracters.isupper():
            upper = True
    
        # Verificar si contiene al menos un número
        if caracters.isnumeric():
            numeric = True

        # Verificar si contiene al menos una caracter especial
        if caracters in string.punctuation:
            especial = True
    
    if lower and upper and numeric and especial:
        resultado = True

    return resultado

# La función debe devolver un valor booleano