'''EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
todas las posibles combinaciones)'''

# Pedir tres medidas
medA = int(input('Escriba la medida de la pieza A '))
medB = int(input('Escriba la medida de la pieza B '))
medC = int(input('Escriba la medida de la pieza C '))

# Comprobar que la medida de todas las piezas son mayores que la suma de las 2 restantes
if medA < medB + medC:
    if medB < medA + medC:
        if medC < medB + medA:
            print('Con las piezas presentadas se puede contruir un triángulo')
        else:
            print('Con las piezas presentadas NO se puede contruir un triángulo')
    else:
        print('Con las piezas presentadas NO se puede contruir un triángulo')
else:
    print('Con las piezas presentadas NO se puede contruir un triángulo')