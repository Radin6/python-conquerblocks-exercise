'''CALCULADORA DE AHORROS:
El objetivo calcular tus ahorros anuales. 
Calcular cuánto puede ahorrar una persona dado sus ingresos por hora, sus horas trabajadas y su gasto de vida semanal.'''

# 1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por pantalla de tipo: ‘Hola <Nombre>’

nombre = input('Dime tu nombre ')
print('Hola', nombre)

# 2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables diferentes
gano_hora = float(input('¿Cuántas ganas por hora? '))
horas_sem = float(input('¿Cuántas horas semanales trabajaste? '))

# 3. Multiplica ambas variables para obtener el salario semanal
gano_semana = gano_hora*horas_sem

# 4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.
gano_anual = gano_semana*4*12

# 5. Ahora imprime por pantalla un mensaje del tipo: ‘<Nombre> tiene unas ganancias anuales de: <cantidad> euros’
print(nombre, ' tiene unas ganancias anuales de:', gano_anual, ' euros')

# 6. Pide los gastos semanales por pantalla y guárdalos en una variable.
gasto_semana = float(input('¿Cuánto gastas a la semana? '))

# 7. Calcula el gasto anual 
gasto_anual = gasto_semana*4*12

# 8. ¡Recuerda añadir comentarios sobre lo que esta haciendo cada parte del código!
# 9. Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.
# 10. Imprime los resultados por pantalla
print(nombre, 'tiene gastos anuales por:', gasto_anual)
print('Por lo tanto su ganancia neta es:', gano_anual-gasto_anual)

'''¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus 
gastos a 3/4 de lo que gastaba antes, tendría suficiente dinero para sus gastos?
(Pista: tan solo necesitas cambiar los valores de las variables de ‘horas trabajadas por semana’ y 
‘gastos semanales’)'''
print('------------------------------')
print('''Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus 
gastos a 3/4 de lo que gastaba antes, el resultado sería:''')
gano_semana = 25*gano_hora
gasto_semana = gasto_semana*(3/4)

if gano_semana > gasto_semana:
    print('Sí, serían suficientes las ganancias')
    print('La ganancia neta semanal sería', gano_semana-gasto_semana )
else:
    print('No, no serían suficientes las ganancias')
    print('La ganancia neta semanal sería', gano_semana-gasto_semana )
