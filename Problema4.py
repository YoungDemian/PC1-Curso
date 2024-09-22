
n = int(input("Introduce un número entero positivo, N: "))
if n > 0:
    suma_rango = sum(range(1, n + 1))
    suma_formula = n * (n + 1) // 2
    print(f"La suma de los enteros desde 1 hasta {n} calculada con el rango es: {suma_rango}")
    print(f"La suma de los enteros desde 1 hasta {n} calculada con la fórmula es: {suma_formula}")
    if suma_rango == suma_formula:
        print("Ambos resultados coinciden. El cálculo es correcto.")
    else:
        print("Los resultados no coinciden. Revisa los cálculos.")
else:
    print("El número debe ser un entero positivo.")
