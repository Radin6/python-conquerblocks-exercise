'''DECLARACION DE LA RENTA:
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros 
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA TIPO IMPOSITIVO
Menos de 15.000 eu 5%
Entre 15.000 y 25.000 eu 15%
Entre 25.000 y 35.000 eu 20%
Entre 35.000 y 60.000 eu 30%
Más de 60.000 eu 45%
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo 
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.'''

# 1. Pedir datos: Edad y cuanto cobra

edad = int(input('Ingrese su edad'))
sueldo = int(input('Ingrese cual es su salario'))

# Sueldo anual
sueldoA = 12*sueldo

#

if sueldo > 1000 and edad >= 18:
    print('Usted es suseptible al cobro de impuestos')
    print('-----------------------------------------')
    if sueldoA < 15000:
        print('Se le cobrará un 5% de impuestos, lo que es igual a: \n', sueldoA*0.05)
    elif 15000 < sueldoA < 25000:
        print('Se le cobrará un 15% de impuestos, lo que es igual a: \n', sueldoA*0.15)
    elif 25000 < sueldoA < 35000:
        print('Se le cobrará un 25% de impuestos, lo que es igual a: \n', sueldoA*0.25)
    elif 35000 < sueldoA < 60000:
        print('Se le cobrará un 30% de impuestos, lo que es igual a: \n', sueldoA*0.3)
    elif 60000 < sueldoA:
        print('Se le cobrará un 45% de impuestos, lo que es igual a: \n', sueldoA*0.45)