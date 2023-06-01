# empresa = {nombre_empleado: salario, departamento}

# programa: 
# 1 agregar empleados, 
# 2 actualizar salario, 
# 3 mostrar loista completa de empleados
# 4 calcular promedio salarial por departamento

import statistics

cond1 = 'si' # condición para romper el loop
empresa = {}
promedio = {}

while cond1 == 'si':
    print('\nAgregando nuevo usuario:\n')

    #Pedimos el nombre, salario y deparatamento del empleado
    nombre_empleado = input('Escriba el nombre del empleado:\n')
    salario = int(input("Escriba el salario del empleado:\n"))
    depart = input('Escriba el departamento donde trabaja el empleado:\n')

    # Al hacer esto si no se encuetra el empleado se lo agrega y si está se actualiza
    empresa[nombre_empleado] = {'salario': salario, 'departamento': depart}

    # Si la respuesta es 'si' el loop va a seguir preguntando por nuevos empleados
    cond1 = input('\n¿Desea agregar o actualizar un empleado? si | no:\n')

    # El bucle no va a aparar hasta tener una respuesta 'si' o 'no'
    while cond1 != 'si' and cond1 != 'no':
        print('Respuiesta incorrecta, vuelva a responder correctamente')
        cond1 = input('\n¿Desea agregar o actualizar un empleado? si | no:\n')

    # Si la respuesta a agregar o actualizar un nuevo empleado es 'no'
    if cond1 == 'no':
    
        cond2 = input('¿Desea calcular el promedio salarial por departamento o terminar? promedio | terminar:\n')

        # El bucle no va a aparar hasta tener una respuesta 'promedio' o 'terminar'
        while cond2 != 'promedio' and cond2 != 'terminar':
            print('Respuiesta incorrecta, vuelva a responder correctamente')
            cond2 = input('¿Desea calcular el promedio salarial por departamento o terminar? promedio | terminar:\n')

        # Si la respuesta fué 'promedio' , va a calcular el promedio de salario de cada departamento
        if cond2 == 'promedio':

            # Calcular promedio
            for empleado in empresa.keys(): # Para cada empleado sacamos el salario y departamento
                salario_ = int(empresa[empleado]['salario'])
                depart_ = str(empresa[empleado]['departamento'])

                if depart_ not in promedio.keys():
                    # Iniciamos como lista los salarios que vamos a ir agregando para luego calcular el promedio
                    promedio[depart_] = []

                # Agregamos el salario a la lista dentro del diccionario {promedio}
                promedio[depart_].append(salario_)
            
            # Vamos a ir imprimiendo los promedios por cada departamento
            for depart_ in promedio.keys():
                salario_promedio = statistics.mean(promedio[depart_])
                print(f'Para el departamento {depart_}, el promedio de salario es {salario_promedio}')