'''STRING A LISTA: 
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información: 
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo: 
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos, 
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e 
imprimir la nota media de los alumnos junto con el DNI. 
Supón ahora que tu input es un string como este: 
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n 
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’ 
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI 
de todos los alumnos en ese string.'''
# Import
import string

# Función que calcula la nota promedio del alumno señalado por i (fila).
def nota_promedio(lista_fin_archivos,i):
    notaTot = 0
    notaF = 0
    for f in range(5,8):
        nota = float(lista_fin_archivos[i][f])  # Transformamos el texto a números reales
        notaTot = notaTot + nota
    return (notaTot/3)  # Nota total dividido 3 da el promedio, se puede remplazar el 3 por una variable que indique la cantidad de notas
# Fin Función

# Input
input_pc = '''David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n 
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚'''

# Dividimos el texto en elementos de una lista
archivo_alumnos = input_pc.split('\n')

# Eliminamos todo elemento de la lista que no empiece con una letra en mayúscula
print(archivo_alumnos)
for datos_alumno in archivo_alumnos:
    if datos_alumno[0] not in string.ascii_uppercase[:]:
        archivo_alumnos.pop(archivo_alumnos.index(datos_alumno))

# Convertimos la lista en una lista de listas llamada lista_fin_archivos
# Dividimos elemenos en los espacios para obtener el formato:
# archivo_alumnos = [nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3]
lista_fin_archivos = []

for fila in archivo_alumnos:
    lista_fin_archivos.append(fila.split(' '))  # Dividimos elemenos en los espacios

print('Lista de archivos', lista_fin_archivos)

# El DNI está en la posición 3 . Las notas en 6, 7 y 8
for i in range(len(lista_fin_archivos)):
    print('DNI del alumno:', lista_fin_archivos[i][2], '\tNota promedio:', nota_promedio(lista_fin_archivos,i))