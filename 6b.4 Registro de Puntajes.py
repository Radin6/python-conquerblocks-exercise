
import statistics

# {"jugador nombre": [lista de puntajes]}

dict_juego = {}
break_loop = ""

while break_loop != "no":

    nombre_jugador = input("\nIngrese su nombre \n")
    puntaje = int(input("Ingrese su puntaje \n"))

    if nombre_jugador not in dict_juego:
        dict_juego[nombre_jugador] = []

    dict_juego[nombre_jugador].append(puntaje)

    break_loop = input("\n¿Desea agregar otro puntaje? si | no : ")

    if break_loop == "no":
        break

    while break_loop != "si" and break_loop != "no":
        print("Respuesta incorrecta")
        break_loop = input("\n¿Desea agregar otro puntaje? si | no : ")
print()
for jugador, lista_puntos in dict_juego.items():
    print(f"{jugador}, su promedio de puntaje es: {statistics.mean(lista_puntos)}, y su puntaje más alto es: {max(lista_puntos)}")

print(f"La cantidad de Jugadores es: {len(dict_juego.keys())}")