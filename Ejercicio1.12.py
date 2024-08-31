# Solicitar al usuario que ingrese una lista de números separados por espacios
entrada = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números
numeros = list(map(float, entrada.split()))

# Implementar el algoritmo de ordenamiento de burbuja
n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Intercambiar los elementos si están en el orden incorrecto
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Imprimir la lista ordenada
print("La lista ordenada es:", numeros)
