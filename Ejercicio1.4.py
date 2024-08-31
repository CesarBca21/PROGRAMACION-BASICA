# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingresa el valor de n (entre 1 y 50): "))

# Verificar que n esté en el rango permitido
if n < 1 or n > 50:
    print("El valor de n debe estar entre 1 y 50.")
else:
    # Inicializar los primeros dos números de la secuencia de Fibonacci
    a, b = 0, 1

    # Imprimir los primeros n números de la secuencia
    print("Los primeros", n, "números de la secuencia de Fibonacci son:")

    for i in range(n):
        print(a, end=" ")  # Imprimir el número actual
        a, b = b, a + b    # Calcular el siguiente número de Fibonacci

    print()  # Nueva línea al final de la secuencia
