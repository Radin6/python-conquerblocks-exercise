'''
Hannah Neise: 8 minutos 3 segundos y 10 centésimas
Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
'''
print('''
Competición de skeleton de las olimpiadas de invierno
Te pedimos ingresar los datos de los 3 finalistas
''')
print('-----------------------')
fina1_nom = 'Hannah Neise:'
print(fina1_nom)
fina1_min = input('¿En cuántos minutos terminó? ')
fina1_min = float(fina1_min)
fina1_seg = input('¿En cuántos segundos terminó? ')
fina1_seg = float(fina1_seg)
fina1_cen = input('¿En cuántas centésimas terminó? ')
fina1_cen = float(fina1_cen)

print('-----------------------')
fina2_nom = 'Jackie Narracott:'
print(fina2_nom)
fina2_min = input('¿En cuántos minutos terminó? ')
fina2_min = float(fina2_min)
fina2_seg = input('¿En cuántos segundos terminó? ')
fina2_seg = float(fina1_seg)
fina2_cen = input('¿En cuántas centésimas terminó? ')
fina2_cen = float(fina2_cen)

print('-----------------------')
fina3_nom = 'Kimberley Bos:'
print(fina3_nom)
fina3_min = input('¿En cuántos minutos terminó? ')
fina3_min = float(fina3_min)
fina3_seg = input('¿En cuántos segundos terminó? ')
fina3_seg = float(fina3_seg)
fina3_cen = input('¿En cuántas centésimas terminó? ')
fina3_cen = float(fina3_cen)

# Convertimos los min, seg y centésimas a segundos totales = seg_tot

fina1_seg_tot = fina1_min*60 + fina1_seg + fina1_cen/60
fina2_seg_tot = fina2_min*60 + fina2_seg + fina2_cen/60
fina3_seg_tot = fina3_min*60 + fina3_seg + fina3_cen/60

# Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en metros por segundo.

fina1_vel_med = 100/fina1_seg_tot
fina2_vel_med = 100/fina2_seg_tot
fina3_vel_med = 100/fina3_seg_tot

# Imprime los resultados por pantalla
print('-----------------------')
print('Para ', fina1_nom, ', los segundos totales que le tomó la competición fueron', fina1_seg_tot,)
print(' y su velocidad media fué de ', fina1_vel_med, 'metros por segundo')
print('-----------------------')
print('Para ', fina2_nom, ', los segundos totales que le tomó la competición fueron', fina2_seg_tot,)
print(' y su velocidad media fué de ', fina2_vel_med, 'metros por segundo')
print('-----------------------')
print('Para ', fina3_nom, ', los segundos totales que le tomó la competición fueron', fina3_seg_tot,)
print(' y su velocidad media fué de ', fina3_vel_med, 'metros por segundo')