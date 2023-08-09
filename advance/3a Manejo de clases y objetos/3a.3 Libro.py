'''LIBRO
Crea una clase "Libro" con atributos como título, autor y año de publicación.
Luego, crea varios objetos Libro y muestra su información.'''

class Libro:
    def __init__(self, titulo, autor, public):
        self.titulo = titulo
        self.autor = autor
        self.public = public

libro1 = Libro("Cien años de soledad", "Marquez", "1991")
libro2 = Libro("El tunel", "Ernesto Sabato", "1948")

print(f'El libro {libro1.titulo} fué escrito por {libro1.autor} en {libro1.public}')
print(f'El libro {libro2.titulo} fué escrito por {libro2.autor} en {libro2.public}')