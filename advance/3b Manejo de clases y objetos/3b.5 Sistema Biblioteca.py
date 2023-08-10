'''SISTEMA DE GESTION DE BIBLIOTECA
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''

class Libro:
    def __init__(self, titulo, autor, numE):
        self.titulo = titulo
        self.autor = autor
        self.numE = numE

class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.librosP = []

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarL(self, libro):
        self.libros.append(libro)
        print(f"\nSe ha agregado: {libro.numE} libros, con título: {libro.titulo} a la Biblioteca")

    def prestarL(self, usuario, tituloBuscado):
        for nLibro in self.libros:
            if tituloBuscado == nLibro.titulo and nLibro.numE > 0:
                usuario.librosP.append(tituloBuscado)
                nLibro.numE -= 1
                print(f"\nEl libro {tituloBuscado} ha sido prestado a {usuario.nombre}")
                return
            
        print(f"\nNo se ha encontrado el libro {tituloBuscado}")

    def devolverL(self, usuario, tituloDevolver):

        if tituloDevolver in usuario.librosP:
            usuario.librosP.remove(tituloDevolver)

            for libro in self.libros:
                if libro.titulo == tituloDevolver:
                    libro.numE += 1
                    print(f"\nEl libro {tituloDevolver} ha sido devuelto exitosamente")
                    return
                
        print(f"No se ha encontrado el libro {tituloDevolver}")

    def mostrarInvent(self):
        print("\nMostrando inventario:")
        for libro in self.libros:
            print(f"Para {libro.titulo} escrito por {libro.autor} se encuentran {libro.numE} ejemplares")

# Dando valores e inicializando
libro1 = Libro("Un cuento perfecto","E. Benavent", 3)
libro2 = Libro("Atomic habits","James Clear", 5)
libro3 = Libro("El problema final","Arturo Reverte", 2)

usuario1 = Usuario("Juan", 1)
usuario2 = Usuario("Pedro", 2)
usuario3 = Usuario("David", 3)

biblioteca = Biblioteca()

# Probando

biblioteca.agregarL(libro1)
biblioteca.agregarL(libro2)
biblioteca.mostrarInvent()
biblioteca.prestarL(usuario2, libro3.titulo)
biblioteca.agregarL(libro3)
biblioteca.mostrarInvent()
biblioteca.prestarL(usuario2, libro3.titulo)
biblioteca.mostrarInvent()
biblioteca.prestarL(usuario1, libro3.titulo)
biblioteca.prestarL(usuario3, libro3.titulo)
biblioteca.mostrarInvent()
biblioteca.devolverL(usuario2, libro3.titulo)
biblioteca.mostrarInvent()