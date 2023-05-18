#ANALISIS DE VENTAS:

ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventaXdia = []


# Por cada día de la semana vamos agregando las ventas totales
for dia in dias_semana:
    ventas_total_dia = 0

    ind = dias_semana.index(dia)
    for n in range(0 + ind, len(ventas), 7):
        ventas_total_dia += ventas[n]
    ventaXdia.append([ventas_total_dia, dia])

print(ventaXdia)
print(max(ventaXdia))
   