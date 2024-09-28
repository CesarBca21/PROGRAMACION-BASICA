# Contador de palabras en un texto
texto = input("Ingresa un texto: ").lower()  # Convertimos todo a minúsculas para evitar diferencias por mayúsculas
palabras = texto.split()  # Separamos el texto en palabras
contador = {}

# Contamos la frecuencia de cada palabra
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

# Imprimimos el contenido del diccionario
for palabra, frecuencia in contador.items():
    print(f"{palabra}: {frecuencia}")
