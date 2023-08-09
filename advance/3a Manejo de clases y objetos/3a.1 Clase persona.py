'''CLASE PERSONA
Define una clase Persona con atributos como nombre, edad y profesión.
Luego, crea varios objetos de esta clase y muestra su información.'''

class persona:
    def __init__ (self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

persona1 = persona("Juan","37","Carpintero")
persona2 = persona("Pedro","31","Operario")

print(f'{persona1.nombre} tiene {persona1.edad} años y es {persona1.profesion}')
print(f'{persona2.nombre} tiene {persona2.edad} años y es {persona2.profesion}')