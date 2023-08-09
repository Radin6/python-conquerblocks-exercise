'''COCHE 
Crea una clase "Coche" con atributos como marca, modelo y año. 
Implementa un método para encender el coche y otro para apagarlo (puedes 
simulae el encendido y apagado con una variable booleana)'''

class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False
    
    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

mi_auto = Coche("Mitsubishi", "Lancer", 1990)
print("¿Está encendido?", mi_auto.encendido)
mi_auto.encender()
print("¿Está encendido?", mi_auto.encendido)
mi_auto.apagar()
print("¿Está encendido?", mi_auto.encendido)