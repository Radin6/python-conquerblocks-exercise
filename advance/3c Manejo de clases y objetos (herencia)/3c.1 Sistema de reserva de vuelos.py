# Crea un sistema de clases que permita a los usuarios realizar reservas de vuelos

'''
- Clase base: `Vuelo`
 - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
 - Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.'''

class Vuelo:
    def __init__(self, nro_vuelo, origen, destino, cap_max):
        self.nro_vuelo = nro_vuelo
        self.origen = origen
        self.destino = destino
        self.cap_max = cap_max
        self.list_pasajeros = []

    def agregar(self, pasajero):
        if self.cap_max > len(self.list_pasajeros):
            self.list_pasajeros.append(pasajero)
            print(f"Se agregó a el pasajero {pasajero} al vuelo {self.nro_vuelo}")
        else:
            print(f"Se ha alcanzado la capacidad máxima para el vuelo {self.nro_vuelo}, no se puede agregar el pasajero")

    def disponibilidad(self):
        if len(self.list_pasajeros) == self.cap_max:
            print(f"La capacidad de pasajeros está completa para el vuelo {self.nro_vuelo}")
        else:
            disponibles = self.cap_max - len(self.list_pasajeros)
            print(f"Se encuentran disponibles {disponibles} asientos para el vuelo {self.nro_vuelo}")


class VueloEspecial(Vuelo):
    def __init__(self, nro_vuelo, origen, destino, cap_max, motivo):
        super().__init__(nro_vuelo, origen, destino, cap_max)
        self.motivo = motivo

# Probando el script

# inicializamos los vuelos
vuelo1 = Vuelo(123, "Barcelona", "Madrid", 2)
vuelo2 = Vuelo(999, "Berlin", "Catania", 3)
vuelo3 = Vuelo(771, "Buenos Aires", "Lima", 4)

# agregamos los pasajeros
print("\nagregamos los pasajeros")
vuelo1.agregar("Pedro")
vuelo1.agregar("Pablo")
vuelo1.agregar("Joel")
vuelo2.agregar("Nico")
vuelo2.agregar("Jose")
vuelo3.agregar("Marcos")

# disponibilidad
print("\ndisponibilidad")
vuelo1.disponibilidad()
vuelo2.disponibilidad()
vuelo3.disponibilidad()

# vuelos especiales
print("\nvuelos especiales")
vuelo_especial = VueloEspecial(222, "NY", "MEL", 5, "negocios")
vuelo_especial.agregar("Gabriel")
print(f"El motivo del vuelo es {vuelo_especial.motivo}")
vuelo_especial.disponibilidad()

