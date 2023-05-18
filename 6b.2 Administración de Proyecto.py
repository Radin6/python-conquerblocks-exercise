
# Tarea (descripción, responsable)

dict_tareas = {}
break_loop = ""

while break_loop != "no":
    tarea = input("\nIngrese la Tarea \n")
    responsable = input("Agregue o Modifique el Responsable de la tarea \n")
    descrip = input("Ingrese o Modifique la Descripción de la tarea \n")

    dict_tareas[tarea] = {"responsable": responsable, "descripción": descrip}

    break_loop = input("\n¿Desea modificar/agregar otra tarea? si | no : ")

    if break_loop == "no":
        break

    while break_loop != "si" and break_loop != "no":
        print("Respuesta incorrecta")
        break_loop = input("\n¿Desea agregar otra tarea? si | no : ")

for tarea in dict_tareas.keys():
    print(f"Para la tarea: {tarea}, el responsable es: {dict_tareas[tarea]['responsable']}, y la descripción es: {dict_tareas[tarea]['descripción']}")