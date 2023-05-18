# VALIDAR ACCESO A UN SITIO WEB:
# Verificar si contraseña y usuario ingresados son correctos

# Import
import random
import string

# Iniciar y definir
usuario_contra = []

## Generar contraseñas
# Función para crear una contraseñas con caracteres aleatorios
def crear_contra():
    contra1 = ''
    num_letras_simbolos = string.ascii_letters + '123456789' + '+=!-_*$%'
    
    # La longitud de la contraseña es de 6
    for n in range(6):
                    #Elige número, letras y símbolos en una posición aleatoria
        contra1 += num_letras_simbolos[random.randint(0,len(num_letras_simbolos)-1)]
    #devuelve la contraseña generada
    return contra1

## Generar usuarios
# Crear una lista de nombres
nombres = ['nico','andi','matt','marcos','emanuel','pepe','messi','jose', 'alexis', 'carlos']

## Crear lista de los usuarios y contraseñas aleatorias

for nombre in nombres:
    usuario_contra.append([nombre,crear_contra()])

print(usuario_contra)

# Ingresando su propio usuario y contraseña dentro de la lista aleatoria
cantidad = range(len(usuario_contra)) # cantidad de [usuario, contraseña]
ok = False

while ok == False:
    ok = True
    usuario_new = input('>>> Ingrese su nombre de usuario para registrarse\n')
    for x in cantidad:
        if usuario_contra[x][0] == usuario_new:
            print('>>> Ya se encuentra alguien registrado con ese nombre de usuario...')
            print('Vuelva a intentar\n')
            ok = False
            break

contra_new = str(input('Ingrese su contraseña a registrar por favor ...\n'))

usuario_contra.append([usuario_new, contra_new])

# Ingresar usuario y contraseña
cantidad = range(len(usuario_contra)) # cantidad nueva de [usuario, contraseña] 
bool_correco = False

print('############################')
print('Bienvenido...')

while bool_correco == False:
    z = 0
    usuario = input('<<< Ingrese su nombre de usuario por favor ...\n')
    for x in cantidad:
        if usuario_contra[x][0] == usuario:
            z = x
            break

    if usuario_contra[z][0] == usuario:
        print('<<< El usuario ingresado es correcto')
        contra = input('Ingrese su contraseña por favor ...\n')
            
        if usuario_contra[z][1] == contra:
            print('<<< La contraseña ingresada es correcta, ingresando al sistema ...')
            bool_correco = True
        else:
            print('<<< La contraseña ingresada es incorrecta, acceso denegado')
            print('Vuelva a intentar\n')
    else:
        print('<<< El usuario ingresado es incorrecto, acceso denegado')