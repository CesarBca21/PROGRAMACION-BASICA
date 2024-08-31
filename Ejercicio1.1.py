# Inicializar la variable para la suma
suma_pares = 0

# Usar un ciclo for para recorrer los números del 1 al 100
for numero in range(1, 101):
    # Verificar si el número es par
    if numero % 2 == 0:
        # Sumar el número par a la variable suma_pares
        suma_pares += numero

# Imprimir el resultado
print("La suma de todos los números pares del 1 al 100 es:", suma_pares)
