# Solicitar al usuario que ingrese una lista de números separados por espacios
entrada = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números
numeros = list(map(float, entrada.split()))

# Encontrar el número mayor y el número menor usando max() y min()
numero_mayor = max(numeros)
numero_menor = min(numeros)

# Imprimir los resultados
print(f"El número mayor en la lista es: {numero_mayor}")
print(f"El número menor en la lista es: {numero_menor}")
