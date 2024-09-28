# Registro de temperaturas diarias
temperaturas = []

for dia in range(1, 8):
    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append((dia, temp))

# Calcular la temperatura promedio
promedio = sum(temp[1] for temp in temperaturas) / len(temperaturas)

# Imprimir el registro y el promedio
print("\nRegistro de temperaturas diarias:")
for dia, temp in temperaturas:
    print(f"Día {dia}: {temp}°C")

print(f"\nTemperatura promedio de la semana: {promedio:.2f}°C")
