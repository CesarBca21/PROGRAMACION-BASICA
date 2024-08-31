# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")

# Inicializar una cadena vacía para almacenar el texto invertido
texto_invertido = ""

# Recorrer cada carácter en la cadena de texto en orden inverso
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

# Imprimir el texto invertido
print("La cadena invertida es:", texto_invertido)
