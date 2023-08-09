import Programa1
import Programa2

while True:
    try:
        num = Programa2.decir_favorito()

    except FileNotFoundError:
        print("No se encontró su número favorito, vuelva a probar...")

    else:
        print(f"Sé cuál es tu número favorito… es: {num}")
        break

    print("-----------")
    Programa1.grabar_favorito()