# Solicitar al usuario que ingrese un número entero
numero = input("Ingresa un número entero: ")

# Inicializar la suma de los dígitos en 0
suma_digitos = 0

# Recorrer cada carácter en la cadena del número
for digito in numero:
    # Verificar si el carácter es un dígito
    if digito.isdigit():
        # Convertir el carácter a entero y sumarlo
        suma_digitos += int(digito)

# Imprimir la suma de los dígitos
print("La suma de los dígitos es:", suma_digitos)
