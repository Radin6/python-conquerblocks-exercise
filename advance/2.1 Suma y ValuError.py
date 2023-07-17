'''SUMA Y VALUEERROR
Un problema común al solicitar una entrada numérica ocurre cuando las
personas ingresan texto en lugar de números. Cuando intentas convertir la
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que
solicite dos números. Suma los números y muestra el resultado. Captura el
ValueError si alguno de los valores de entrada no es un número e imprime un
mensaje de error amigable. Prueba tu programa ingresando dos números y
luego ingresando texto en lugar de un número. Envuelve tu código del en un
bucle while para que el usuario pueda continuar ingresando números incluso
si comete un error ingresando texto en lugar de un número.'''

while True:
    num1 = input("Ingresa el primer número:\n")
    if num1 == "s":
        break
    num2 = input("Ingresa el segundo número:\n")
    if num2 == "s":
        break
    
    try:
        resultado = int(num1) + int(num2)
    except ValueError:
        print("ERROR: Solo debe ingresar números")
    else:
        print("El resultado es: ", resultado)