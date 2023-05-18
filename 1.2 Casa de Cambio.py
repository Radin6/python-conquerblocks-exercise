euros = input('Escriba la cantidad de Euros a cambiar ')
euros = float(euros)

para_casa_eur = euros*0.1
para_cliente_eur = euros*0.9

print('Se reciben ', euros, 'euros')
print('El cambio es de 1,2 dólares por euro')
print('La casa se queda con una comisión de ', para_casa_eur, 'euros')
print('Usted recibe ', para_cliente_eur*1.2 , 'dólares')
