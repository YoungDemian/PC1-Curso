num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("\nElige una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
print("3. Salir")
opcion = input("\nIntroduce el número de la opción deseada: ")
if opcion == '1':
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")
elif opcion == '2':
    resta = num1 - num2
    print(f"La resta de {num1} menos {num2} es: {resta}")
elif opcion == '3':
    print("Saliendo del programa...")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")
