## Ejercicio 3: Contraseña segura ##
import creador
import validador

while True:
    respuesta1 = input('¿Desea generar o verificar si una contraseña es segura? generar | verificar | terminar :\n')

    if respuesta1 == 'verificar':
        contra = input('Ingrese la contraseña\n')
        resultado = validador.validar_contraseña(contra)
        if resultado:
            print("Su contraseña es válida")

        else:
            print("Su contraseña NO es válida")

    elif respuesta1 == 'generar':
        long = int(input("Ingrese la longitud que desea (como mínimo 4):\n"))

        # Desea incluir los siguientes: si >> T
        includeUpper = "si" == input("Si desea incluir Mayúsculas escriba: si :\n")
        includeLower = "si" == input("Si desea incluir Minúsculas escriba: si : \n")
        includeNum = "si" == input("Si desea incluir Números escriba: si :\n")
        includeSpecial = "si" == input("Si desea incluir Carácteres especiales escriba: si :\n")

        print(includeLower, includeNum, includeSpecial, includeUpper)

        creador.generar_contraseña(long, 
                       includeUpper, 
                       includeLower, 
                       includeNum, 
                       includeSpecial)
    
    elif respuesta1 == "terminar":
        break