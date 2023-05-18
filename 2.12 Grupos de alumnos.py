'''GRUPOS DE ALUMNOS:
En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
pantalla el grupo que le corresponde a ese alumno.'''

# Import
import string

# Grupo A: Chicas con nombre de E a M, Chicos con nombre A a H y R a Z
# Grupo B: Resto chicas, Resto chicos

# Preguntar si es chica o chico y el nombre
sexo = str(input('¿El alumno es chica o chico? '))
sexo = sexo.title()
nombre = str(input('¿Cuál es el nombre del alumno? '))
nombre = nombre.title()

# Establecer si las Chicas con primera letra del nombre está entre E y M
# Si es así lo establecemos como True
letraEM = string.ascii_lowercase[4:13]
grupoEM = False

# Comprobar si la inicial del nombre está entre E y M incluidas
if nombre[0].lower() in letraEM:
    grupoEM = True

# Establecer si los Chicos con primera letra del nombre está entre A a H o R a Z
# abcdefghijklmnopqrstuvwxyz
# Si es así lo establecemos como True
letraAHRZ = string.ascii_lowercase[:7] + string.ascii_lowercase[17:]
grupoAHRZ = False

# Comprobar si la inicial del nombre está entre A y H o R y Z
if nombre[0].lower() in letraAHRZ:
    grupoAHRZ = True

# Mostrar el grupo que le corresponde al alumno
if sexo == 'Chica' and grupoEM == True:
    print(nombre, 'pertenece al Grupo A')
elif sexo == 'Chica':
    print(nombre, 'pertenece al Grupo B')
elif sexo == 'Chico' and grupoAHRZ == True:
    print(nombre, 'pertenece al Grupo A')
elif sexo == 'Chico':
    print(nombre, 'pertenece al Grupo B')
else:
    print('Se produjo algún error en el ingreso de datos')