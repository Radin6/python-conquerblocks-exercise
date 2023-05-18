'''BOT DE TRADING:
Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
estrictamente por encima de 150 el bot deberá imprimir la orden de vender.'''

# Pedir el precio del producto financiero
precio = int(input('Escribe el precio del producto financiero en dolares: '))

# Resolver con if statement
if precio < 100:
    print('El precio cayó por debajo de 100 dólares, Se disparó un orden de compra')
elif 100 <= precio <= 150:
    print('El precio está en rango de HOLD')
elif precio > 150:
    print('El precio subió por encima de 150 dólares, Se disparó un orden de venta')
else:
    print('Precio introducido invalido')