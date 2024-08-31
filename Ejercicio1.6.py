# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Generar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
