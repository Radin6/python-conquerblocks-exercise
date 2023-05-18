# 22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada
# representa un producto y tiene a su vez las claves "nombre" y "precio" con sus
# respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada producto.
print("\nEjercicio 22")

productos = {"prod1": {"nombre": "Azucar", "precio": 2},"prod2":{"nombre": "Pan", "precio": 1}}

for producto in productos.keys():
    nombre, precio = productos[producto].values()
    print(nombre, precio)

# 23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y
# valor. Imprime el diccionario actualizado.
print("\nEjercicio 23")

productos["prod3"] = {"nombre": "Crema", "precio": 3}
print(productos)

# 24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada
# representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
# respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de
# los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores.
print("\nEjercicio 24")

equipos = {"equipo1": {"nombre": "PSG", "jugadores": ["Messi", "Mbappe"]},
           "equipo2": {"nombre": "Colón", "jugadores": ["Wanchope", "Farías"]},
           "equipo3": {"nombre": "Barcelona", "jugadores": ["Busquets", "Alba"]}}

for nro_equipo, equipo in equipos.items():
    print(equipo["nombre"], equipo["jugadores"])

# 25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
# La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario actualizado.
print("\nEjercicio 25")

equipos["equipo4"] = {"nombre": "Napoli", "jugadores": ["Osimhen", "Simeone", "Lozano"]}

for nro_equipo, equipo in equipos.items():
    print(equipo["nombre"], equipo["jugadores"])

# 26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario
# "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.
print("\nEjercicio 26")

equipos["equipo3"]["jugadores"].append("Gavi")

for nro_equipo, equipo in equipos.items():
    print(equipo["nombre"], equipo["jugadores"])