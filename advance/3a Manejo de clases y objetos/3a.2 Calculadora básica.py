'''CALCULADORA BÁSICA
Crea una clase llamada "Calculadora" con métodos para sumar, restar,
multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones
básicas.'''

class Calculadora:
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return  a - b
    
    def multiplicar(a, b):
        return a * b
    
    def dividir(a, b):
        return a / b

A = int(input("Ingrese el primer número: "))
B = int(input("Ingrese el segundo número: "))

print(f'La suma de {A} y {B} da: ', Calculadora.sumar(A, B))
print(f'La resta de {A} y {B} da: ', Calculadora.restar(A, B))
print(f'La multiplicación de {A} y {B} da: ', Calculadora.multiplicar(A, B))
print(f'La división de {A} y {B} da: ', Calculadora.dividir(A, B))