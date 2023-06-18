# 1. Define una función llamada "saludar" que tome un parámetro "nombre" y muestre un saludo personalizado.
print(f'\nEjercicio 1')
def saludar(nombre):
    print(f'Hola {nombre}!')

saludar('Pedro')

# 2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e imprima la suma de ambos.
print('\nEjercicio 2')
def suma(a,b):
    print(f'La suma de {a} y {b} es: ',a+b)

suma(3,9)
suma(1,8)

# 3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
#parámetros "base" y "altura" y calcule el área de un rectángulo.
print('\nEjercicio 3')
def calcular_area_rectangulo(base, altura):
    print(f'El área de un rectángulo con base {base} y altura {altura} es: {base*altura}')

calcular_area_rectangulo(4,8)

# 4. Define una función llamada "imprimir_lista" que tome una lista como parámetro y la imprima en la consola.
print('\nEjercicio 4')
def imprimir_lista(lista):
    print('La lista es: ', lista)

imprimir_lista([1,2,3])

# 5. Crea una función llamada "es_par" que tome un número como parámetro e imprima True si es par, o False si es impar.
print('\nEjercicio 5')
def es_par(num):
    print(f'El número {num} es par >> ', num%2 == 0)

es_par(2)
es_par(3)

# 6. Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y “cadena2" e imprima la concatenación de ambas cadenas.
print('\nEjercicio 6')
def concatenar_strings(cadena1, cadena2):
    print(f'Si concatenamos {cadena1} y {cadena2} obtenemos >>', cadena1+cadena2)

concatenar_strings('Rompe', 'cabezas')

# 7. Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.
print('\nEjercicio 7')
def obtener_maximo(nums):
    print(f'El mayor número de la lista {nums} es:', max(nums))

obtener_maximo([3,8,5,11])

# 8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.
print('\nEjercicio 8')
def convertir_fahrenheit_a_celsius(fahrenheit):
    print(f'La temperatura de {fahrenheit} grados fahrenheit en celcius es:',(fahrenheit-32)*5/9)

convertir_fahrenheit_a_celsius(111)

# 9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad de una persona.
print('\nEjercicio 9')
def calcular_edad(año_actual, año_nacimiento):
    print(f'Si la persona nació en {año_nacimiento} y ahora es {año_actual}, la edad es', año_actual-año_nacimiento)

calcular_edad(2023, 1991)

# 10. Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor", o False si no lo es.
print('\nEjercicio 10')
def es_divisible(num, divisor):
    print(f'El número {num} es divisible por {divisor} >>',num%divisor == 0)

es_divisible(4,2)
es_divisible(5,3)

# 11. Crea una función llamada "mostrar_info_persona" que tome tres argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
# debe imprimir en la consola la información de una persona en un formato legible.
print('\nEjercicio 11')
def mostrar_info_persona(nombre, edad, ciudad):
    print(f'{nombre} tiene la edad de {edad} años y vive en la ciudad de {ciudad}')

mostrar_info_persona('Daniel', '41', 'Santa Fe')

# 12. Escribe una función llamada "calcular_promedio" que tome una lista de números como parámetro y calcule el promedio de esos números. 
# Si no se proporciona una lista, debe usar una lista vacía por defecto.
print('\nEjercicio 12')
import statistics
def calcular_promedio(lista=[]):
    print(statistics.mean(lista))
calcular_promedio([1,3,8])

# 13. Crea una función llamada "calcular_potencia" que tome dos parámetros "base" y "exponente", y calcule la potencia de la base
# elevada al exponente. Utiliza 2 como valor por defecto para el exponente.
print('\nEjercicio 13')
def calcular_potencia(base, exponente=2):
    print(f'La base {base} con el exponente {exponente} da como resultado:', base**exponente)

calcular_potencia(2)
calcular_potencia(2,4)

# 14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”(y sin valor por defecto) y varios
# argumentos de palabra clave: "edad", "curso" y “promedio" (puedes ponerles como valor por defecto None). La función debe imprimir la
# información del alumno en un formato legible.
print('\nEjercicio 14')
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print(f'El alumno {nombre} cuya edad es {edad} y cursa en {curso}, tiene un promedio de {promedio}')

imprimir_info_alumno('Jose')
imprimir_info_alumno('Pedro', 19)
imprimir_info_alumno('Ariel', 18, 'Lenguas', 8)