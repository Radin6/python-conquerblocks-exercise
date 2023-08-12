'''Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.'''

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)
        self.bono_anual = bono_anual

    def salario_total(self):
        print(f"Salario total de {self.nombre} : {self.salario+self.bono_anual}")

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario, horas_semana):
        super().__init__(nombre, apellido, salario)
        self.horas_semana = horas_semana

    def ganancia_hora(self):
        print(f"El empleado {self.nombre} gana : {self.salario/self.horas_semana} por hora")

# inicializamos a los empleados
empleado1 = EmpleadoTiempoCompleto("Andrés", "Morales", 1000, 200)
empleado2 = EmpleadoTiempoParcial("Jose", "Rodríguez", 600, 20)
empleado3 = EmpleadoTiempoCompleto("Marcos", "Ramos", 1300, 300)

# verificamos salarios total en los empleados TC y salario por hora en empleados TP
print("")
empleado1.salario_total()
empleado2.ganancia_hora()
empleado3.salario_total()
