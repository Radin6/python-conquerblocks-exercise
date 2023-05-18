## Red Social
print("Red Social\n")
# tupla contiene el nombre del usuario y una lista de sus amigos
# eliminar las cuentas duplicadas
# devolver una tupla de tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

red_social_unicos = []
num_mayor = 0

for persona in red_social:
    num_amigos = len(set(persona[1]))
    persona_unicos = (persona[0], num_amigos)
    red_social_unicos.append(persona_unicos)

    if num_amigos > num_mayor:
        num_mayor = num_amigos
        persona_mas_amigos = persona[0]

red_social_unicos = tuple(red_social_unicos)

print(red_social_unicos)
print("La persona con más amigos es:", persona_mas_amigos, "con", num_mayor ,"amigos")

## La Biclioteca
# devuelva una nueva lista de tuplas que contenga el título del libro y el apellido del autor.
print("La Biblioteca\n")
lista_libros = [("El aleph", "Jorge Luis Borges"), 
                ("Cien años de soledad", "Garbriel Garcia Márquez"), 
                ("La ciudad y los perros", "Mario Vargas Llosa")]

lista_libros_nueva = []

for libro in lista_libros:
    nombre_completo = libro[1].split()
    apellido = nombre_completo[-1]
    libro_tupla = (libro[0], apellido)

    lista_libros_nueva.append(libro_tupla)

lista_libros_nueva = tuple(lista_libros_nueva)

print(lista_libros_nueva)

## Datos clientes
# tome las dos bases de datos como listas de tuplas y devuelva una nueva lista de tuplas 
# que contenga solo los clientes que aparecen en ambas bases de datos
# Los clientes se consideran iguales si tienen el mismo nombre
print("Datos clientes\n")

base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria",
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]

base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),
("Luis", "Calle 789", ["Libro4"])]

base_datos_unicos = []

for linea1 in base_datos1:
    for linea2 in base_datos2:
        if linea1[0] == linea2[0]:
            linea3 = linea1 + linea2[1:]
            base_datos_unicos.append(linea3)

print(base_datos_unicos)