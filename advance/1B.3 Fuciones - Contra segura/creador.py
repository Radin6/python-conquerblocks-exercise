# Generar contraseñas seguras de forma aleatoria
# La función debe permitir especificar la longitud de la contraseña y qué tipos de 
# caracteres deben incluirse (por ejemplo, letras mayúsculas, letras 
# minúsculas, números y caracteres especiales).
import random
import string

def generar_contraseña(long_, 
                       includeUpper_ = True, 
                       includeLower_ = True, 
                       includeNum_ = True, 
                       includeSpecial_ = True):
    contra = ""
    n = 0
    caracteres = ""

    if includeUpper_:
        caracteres += string.ascii_uppercase
        contra += random.choice(string.ascii_uppercase)
        n +=1

    if includeLower_:
        caracteres += string.ascii_lowercase
        contra += random.choice(string.ascii_lowercase)
        n +=1

    if includeNum_:
        caracteres += string.digits
        contra += random.choice(string.digits)
        n +=1
    
    if includeSpecial_:
        caracteres += string.punctuation
        contra += random.choice(string.punctuation)
        n +=1

    if long_ < n:
        return print('ERROR: La cantidad de caracteres mínima es:', long_)

    for i in range(long_ - n):
        contra += str(random.choice(caracteres))
    
    contra = ''.join(random.sample(contra, len(contra)))

    return print(contra)

# Para el generador de contraseñas puedes probar a usar los modulos random y string