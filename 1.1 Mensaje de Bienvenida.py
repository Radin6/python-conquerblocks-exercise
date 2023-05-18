msg_b = 'estas usando python'
print(msg_b)
nombre = input('¿Cuál es tu nombre? ')
print('¡Hola,', nombre ,', estas usando python!')

print('¡Hola,'.upper(), nombre.upper() ,', estas usando python!'.upper())

print('¡Hola,'.lower(), nombre.lower() ,', estas usando python!'.lower())

nombre = nombre.replace('.','')

print('¡Hola,', nombre.title() ,', estas usando python!')