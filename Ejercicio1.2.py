# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entre 1 y 20: "))

# Verificar que el número esté en el rango permitido
if numero < 1 or numero > 20:
    print("Número fuera de rango. Debe estar entre 1 y 20.")
else:
    # Inicializar el factorial en 1
    factorial = 1
    # Inicializar un contador
    contador = numero
    
    # Calcular el factorial usando un ciclo while
    while contador > 1:
        factorial *= contador
        contador -= 1
    
    # Imprimir el resultado
    print(f"El factorial de {numero} es: {factorial}")
