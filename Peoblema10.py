def eliminar_elementos(lista):
    nueva_lista = [elemento for i, elemento in enumerate(lista) if i not in (0, 4, 5)]
    return nueva_lista
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
resultado = eliminar_elementos(lista_muestra)
print(resultado)
