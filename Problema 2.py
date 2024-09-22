
consumo = float(input("¿Cuánto fue el total de tu consumo en el restaurante?: "))
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar?): "))
propina = consumo * (porcentaje_propina / 100)
print(f"Debes dejar una propina de: ${propina:.2f}")