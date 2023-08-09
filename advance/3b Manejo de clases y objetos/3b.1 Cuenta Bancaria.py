'''CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.'''


class CuentaBancaria:

    def __init__(self, numCuenta, saldo=0):
        self.saldo = saldo
        self.numCuenta = numCuenta
        
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad}")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad}")
        else:
            print(f"La cantidad a retirar es mayor que el saldo")
         
    def mostrarSaldo(self):
        print(f"Su saldo es de {self.saldo}")

micuenta1 = CuentaBancaria(1,100)
micuenta1.mostrarSaldo()
micuenta1.depositar(100)
micuenta1.mostrarSaldo()
micuenta1.retirar(300)
micuenta1.retirar(30)
micuenta1.mostrarSaldo()