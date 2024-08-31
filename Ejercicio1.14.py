import random

# Solicitar al usuario que ingrese la cantidad de números aleatorios
n = int(input("Ingresa la cantidad de números aleatorios a generar: "))

# Verificar que n sea un número positivo
if n <= 0:
    print("La cantidad de números debe ser un número positivo.")
else:
    # Inicializar una lista vacía para los números aleatorios
    numeros_aleatorios = []

    # Generar n números aleatorios entre 1 y 100
    for _ in range(n):
        numero = random.randint(1, 100)
        numeros_aleatorios.append(numero)

    # Imprimir la lista de números aleatorios
    print("La lista de números aleatorios es:", numeros_aleatorios)
