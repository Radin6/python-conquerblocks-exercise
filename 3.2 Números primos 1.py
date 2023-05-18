'''NUMEROS PRIMOS 1:
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo. '''

veces = 0

for num in range(2,101):
    veces = 0
    for x in range(2,101):
        if num%x == 0:
            veces = veces + 1
    if veces == 1:
        print(num)