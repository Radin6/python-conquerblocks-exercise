'''CALCULO DE NOTAS FINALES
Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna.'''

import numpy as np
import random

# Genero datos al azar:
alumnos = random.randint(3,10)
notas = np.zeros([alumnos,4])

# Función que genera notas al azar de 1 a 10 incluido
def nota_random():
    return random.randint(1,10)

# notas[alumnno] = [nota1, nota2, trabajo_final, particip_clase]
for alumno in range(alumnos):
    notas[alumno] = np.array([nota_random(), nota_random(), nota_random(), nota_random()])

print('Array de notas por alumno:\n', notas)

# nota_final[alumnno] = [nota1*0.3, nota2*0.3, trabajo_final*0.3, particip_clase*0.1]
notas_final = notas.copy()

notas_final[:,:3] *= 0.3
notas_final[:,3] *= 0.1

notas_final = notas_final.sum(1)

# Notas por alumnos en una sola columna
notas_final2 = notas_final.reshape(alumnos,1)

print('Array de notas final por alumno en una columna:\n', notas_final2)

