edad = int(input("Por favor, introduce tu edad: "))
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10
if precio == 0:
    print("La entrada es gratuita.")
else:
    print(f"El precio de la entrada es: ${precio}")
