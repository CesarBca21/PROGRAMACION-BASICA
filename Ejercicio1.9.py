# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")

# Inicializar el contador de palabras
contador_palabras = 0

# Variable para acumular palabras
palabra_actual = ""

# Recorrer cada carácter en la cadena de texto
for caracter in texto:
    # Verificar si el carácter es un espacio
    if caracter == " ":
        # Si encontramos un espacio y hay una palabra acumulada, contarla
        if palabra_actual:
            contador_palabras += 1
            palabra_actual = ""  # Reiniciar la palabra acumulada
    else:
        # Acumulamos los caracteres en la palabra actual
        palabra_actual += caracter

# Contar la última palabra si no termina con un espacio
if palabra_actual:
    contador_palabras += 1

# Imprimir el número de palabras
print(f"El número de palabras en la cadena es: {contador_palabras}")
