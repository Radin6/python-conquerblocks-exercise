'''Una compañía de automóviles vende tres tipos de coche: 
RBM Serie 1, RMB Serie plus, RBM todoterreno. 
Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.'''

# Pedir número venido de Coche 1
print('------------------')
coch1_nom = 'RBM Serie 1'
print('¿Cuántos coches', coch1_nom ,'se vendieron?')
coch1_num = input()
coch1_num = int(coch1_num)

# Pedir número venido de Coche 2
print('------------------')
coch2_nom = 'RMB Serie plus'
print('¿Cuántos coches', coch2_nom ,'se vendieron?')
coch2_num = input()
coch2_num = int(coch2_num)

# Pedir número venido de Coche 3
print('------------------')
coch3_nom = 'RBM todoterreno'
print('¿Cuántos coches', coch3_nom ,'se vendieron?')
coch3_num = input()
coch3_num = int(coch3_num)

# Cantidad a comisionar
com_coch1 = coch1_num*20000*0.03
com_coch2 = coch2_num*35000*0.05
com_coch3 = coch3_num*60000*0.07
com_total = com_coch1 + com_coch2 + com_coch3
print('------------------')
print('La cantidad a comisionar es de ', int(com_total), 'euros')

