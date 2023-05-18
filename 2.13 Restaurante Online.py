'''RESTAURANTE ONLINE:
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente 
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana. 
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la 
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos. 
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus 
ingredientes.'''

# Ingredientes extra como string
extraC = ['Queso Idiazabal','Bacon','Huevo']
extraV = ['Tofu','Cebolla caramelizada']

# 1. Pedir datos: Tipo de hamburguesa y ingredientes extras
error = False
extra = ''
tipo = input('Elige el tipo de hamburgesa: Clasica | Vegana\n')
tipo = tipo.title()

if tipo == 'Clasica':
    extra = input('Desea agregarle algún ingrediente extra?:\
        \n-Queso Idiazabal\n-Bacon\n-Huevo\n')
    if extra.title() not in extraC:
        print('Los ingredientes extra ingresados son incorrectos')
        error = True

elif tipo == 'Vegana':
    extra = input('Desea agregarle algún ingrediente extra?:\
        \n- Tofu\n-Cebolla caramelizada ')
    if extra.title() not in extraV:
        print('Los ingredientes extra ingresados son incorrectos')
        error = True
else:
    print('El tipo de hamburgesa ingresado es incorrecto')
    error = True

extra = extra.title()

# 2. Imprimir por pantalla lo elegido

if error == False:
    print('Usted ha elegido una hamburgesa', tipo, '\nCon ingrediente extra de', extra)
else:
    print('### ERROR ###')