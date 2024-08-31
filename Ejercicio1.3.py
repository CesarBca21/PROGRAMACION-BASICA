# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Inicializar una variable para indicar si es primo
es_primo = True

# Un número menor que 2 no es primo
if numero < 2:
    es_primo = False
else:
    # Verificar si el número tiene divisores distintos de 1 y de sí mismo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

# Mostrar el resultado
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
