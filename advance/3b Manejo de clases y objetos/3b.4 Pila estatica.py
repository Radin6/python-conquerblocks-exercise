'''PILA (STACK) BÁSICA
Crea una clase "Pila" que represente una pila (stack) básica. Implementa
métodos para agregar elementos a la pila, quitar elementos y mostrar el
contenido actual.
Por supuesto, estaré encantado de explicarte qué es un "stack" en el
contexto de la programación y cómo se utiliza en Python.'''

class Pila:

    def __init__(self):
        self.pila = []
    
    def agregar(self, elemento):
        self.pila.append(elemento)
        print(f"Se ha agregado {elemento} a la pila\n")

    def quitar(self):
        elemento = self.pila.pop()
        print(f"Se ha quitado {elemento}\n")

    def mostrar(self):
        print(f"Estado actual de la Pila: {self.pila}\n")

PILA = Pila()

PILA.agregar(6)
PILA.agregar(9)
PILA.mostrar()
PILA.quitar()
PILA.mostrar()