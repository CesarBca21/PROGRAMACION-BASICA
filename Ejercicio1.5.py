# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Recorrer cada carácter en la cadena de texto
for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

# Imprimir el número total de vocales
print(f"El número de vocales en la cadena es: {contador_vocales}")
