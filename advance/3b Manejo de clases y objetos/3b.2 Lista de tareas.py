'''LISTA DE TAREAS
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea, marcar una tarea como
completada y mostrar todas las tareas'''

class ListaTareas:

    def __init__(self, tPendientes):
        self.tPendientes = tPendientes
        self.tHechas = []
    
    def agregarT(self, nuevaTarea):
        self.tPendientes.append(nuevaTarea)
        print(f"Se agregó la tarea {nuevaTarea}")
    
    def hechaT(self, tareaHecha):
        if tareaHecha in self.tPendientes:
            self.tPendientes.remove(tareaHecha)
            self.tHechas.append(tareaHecha)
            print(f"La tarea {tareaHecha} está completada")
    
    def mostrarT(self):
        print(f"Las tareas pendientes son {self.tPendientes} y las hechas son {self.tHechas}")


lista1 = ListaTareas(["limpiar", "correr", "trabajar"])
lista1.mostrarT()
lista1.agregarT("jugar")
lista1.mostrarT()
lista1.hechaT("trabajar")
lista1.mostrarT()