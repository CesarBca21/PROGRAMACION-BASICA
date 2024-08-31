# Solicitar al usuario que ingrese una lista de números separados por espacios
entrada = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números
numeros = list(map(float, entrada.split()))

# Calcular la suma de todos los elementos de la lista
suma = sum(numeros)

# Imprimir el resultado
print(f"La suma de todos los elementos en la lista es: {suma}")
