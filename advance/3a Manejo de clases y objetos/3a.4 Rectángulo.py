'''RECTÁNGULO 
Crea una clase "Rectangulo" con atributos de largoitud y ancho. Implementa 
un método para calcular el área y el perímetro del rectángulo.'''

class Rectangulo:
    def __init__(self, largo, ancho):
        self.area = largo*ancho
        self.perimetro = (ancho+largo)*2

largo = int(input("Ingresa el largo: "))
ancho = int(input("Ingresa el ancho: "))

calcular = Rectangulo(largo, ancho)
print(f'El área del triangulo es {calcular.area} y el perímetro es {calcular.perimetro}')