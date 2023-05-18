
# {"estudiante nombre": [lista de fechas de asistencia]}

dict_asistencia = {}
break_loop = ""

while break_loop != "no":

    nombre_alumno = input("\nIngrese el nombre del alumno \n")
    fechas_asist = input("Ingrese la fecha de asistencia \n")

    if nombre_alumno not in dict_asistencia:
        dict_asistencia[nombre_alumno] = []

    dict_asistencia[nombre_alumno].append(fechas_asist)

    break_loop = input("\n¿Desea agregar o modificar fechas de asistencia? si | no : ")

    if break_loop == "no":
        break

    while break_loop != "si" and break_loop != "no":
        print("Respuesta incorrecta")
        break_loop = input("\n¿Desea agregar o modificar fechas de asistencia? si | no : ")

for alumno, fechas in dict_asistencia.items():
    print(f"Para el alumno {alumno}, las fechas de asistencia fueron {fechas}")