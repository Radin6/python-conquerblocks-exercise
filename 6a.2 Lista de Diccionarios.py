# 18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario
# representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos
# valores. Recorre la lista e imprime el nombre y edad de cada estudiante.
print("\nEjercicio 18")

estudiantes = [{"nombre": "Dario", "edad": 20}, {"nombre": "María", "edad": 21}]

for estudiante in estudiantes:
    nombre, edad = estudiante.values()
    print(nombre, edad)

# 19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las
# mismas claves "nombre" y "edad". Imprime la lista actualizada.
print("\nEjercicio 19")

estudiantes.append({"nombre": "Juan", "edad": 23})
print(estudiantes)

# 20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
print("\nEjercicio 20")

estudiantes.pop(1)
print(estudiantes)

#21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. Imprime la lista actualizada.
print("\nEjercicio 21")

estudiantes[0]["edad"] = 19
print(estudiantes)