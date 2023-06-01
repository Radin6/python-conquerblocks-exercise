'''Implementa un programa en Python que permita registrar los votos, 
mostrar la lista completa de candidatos y sus votos, encontrar al 
candidato ganador (con más votos) y calcular el porcentaje de votos que 
obtuvo cada candidato'''

# porcentaje[nombre] = {porc_cand}

votos = {'Daniel': 9, 'Jose': 5, 'Julia': 12, 'Pedro': 3, 'Juana': 13}

votos_totales = sum(votos.values())

nombre_ganador = max(votos, key=votos.get)

for nombre, nro_votos in votos.items():

    porcentaje = nro_votos*100/votos_totales
    print(f'{nombre} obtuvo {nro_votos} votos y un porcentaje de {porcentaje}')

print(f'\nEL/La ganador/a es {nombre_ganador}')


