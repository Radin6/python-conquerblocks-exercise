'''BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media. 
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que 
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no'''

# Pedir nombre, edad y nota media
nom = input('Introduce tu nombre ')
edad = int(input('Introduce tu edad '))
nota = float(input('Introduce tu nota media '))

# Calcular si puede optar a la beca
if edad > 17 and edad < 21:
    if nota >= 8:
        print(nom.title(), 'eres apto para la beca' )
    else:
        print(nom.title(), 'NO eres apto para la beca' )
else:
    print(nom.title(), 'NO eres apto para la beca' )