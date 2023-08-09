'''TIENDA ONLINE
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.'''

class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.listaTienda = []

    def agregarP(self, producto):
        self.listaTienda.append(producto)
        print(f"Se han adherido {producto.cantidad} {producto.nombre}\n")

    def mostrarP(self):
        print(f"El inventario de la Tienda actualmente es: ")
        for producto in self.listaTienda:
            print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
        print()

    def compraP(self, productoN, cantidadC):

        for produc in self.listaTienda:
            if produc.nombre in productoN:
                if produc.cantidad >= cantidadC:
                    produc.cantidad -= cantidadC
                    print(f"Compra exitosa: el gasto total es de {cantidadC*produc.precio} EUR")
                    break
                else:
                    print("La cantidad en stock no es suficiente")
                    break
    
        print(f"{productoN} no existe\n")


tienda = Tienda()
producto1 = Producto("zapatillas", 100, 5)
producto2 = Producto("gorras", 15, 22)
producto3 = Producto("buzos", 50, 10)

tienda.agregarP(producto1)
tienda.agregarP(producto2)
tienda.agregarP(producto3)
tienda.mostrarP()
tienda.compraP("jugo", 10)
tienda.compraP("gorras", 30)
tienda.compraP("zapatillas", 2)
tienda.mostrarP()

