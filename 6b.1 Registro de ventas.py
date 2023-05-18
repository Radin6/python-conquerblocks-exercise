## REGISTRO DE VENTAS
dict_productos = {}
break_loop = ""

while break_loop != "no":
    nombre_prod = input("Ingrese el nombre del producto \n")
    cant_vendida = input("¿Cuanto se vendió en la venta actual? \n")

    if nombre_prod not in dict_productos:
        dict_productos[nombre_prod] = 0

    dict_productos[nombre_prod] += int(cant_vendida)

    break_loop = input("¿Desea agregar otro? si | no : ")

    if break_loop == "no":
        break

    while break_loop != "si" and break_loop != "no":
        print("Respuesta incorrecta")
        break_loop = input("¿Desea agregar otro? si | no : ")

for prod, cant in dict_productos.items():
    print(f"Para el producto {prod}, la cantidad vendida fué {cant}")