'''DADO 
Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras. 
Implementa un método para lanzar el dado y mostrar el resultado (quizás te 
convenga usar el modulo random)'''
import random

class Dado:
    def __init__(self):
        self.tirar = random.randint(1,6)

dad0 = Dado()

print(dad0.tirar)