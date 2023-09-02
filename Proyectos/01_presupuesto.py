# Calcular el promedio del presupuesto por trimestre

# Solicitamos al usuario y almacenamos valores de cada mes en Variables
budget_january = int(input('Ingresa el valor del presupuesto de Enero: '))
budget_february = int(input('Ingresa el valor del presupuesto de Enero: '))
budget_march = int(input('Ingresa el valor del presupuesto de Enero: '))

# Calculamos en promedio del presupuesto de los tres meses
avg_budget = float((budget_january + budget_february + budget_march) / 3)

# Mostramos en pantalla el promedio del presupuesto para los tes meses solcitados
print(f"El promedio es: {avg_budget}")
