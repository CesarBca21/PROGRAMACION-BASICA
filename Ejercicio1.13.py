# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")

# Solicitar al usuario que ingrese el carácter a contar
caracter_a_contar = input("Ingresa el carácter a contar: ")

# Verificar que solo se haya ingresado un solo carácter
if len(caracter_a_contar) != 1:
    print("Debes ingresar exactamente un carácter.")
else:
    # Inicializar el contador en 0
    contador = 0

    # Recorrer cada carácter en la cadena de texto
    for caracter in texto:
        # Incrementar el contador si el carácter coincide
        if caracter == caracter_a_contar:
            contador += 1

    # Imprimir el número de veces que aparece el carácter
    print(f"El carácter '{caracter_a_contar}' aparece {contador} veces en la cadena.")
