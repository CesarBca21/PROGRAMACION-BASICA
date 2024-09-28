# Diccionario de traducción de palabras
traducciones = {}

continuar = "s"
while continuar.lower() == "s":
    palabra = input("Ingresa una palabra en español: ").lower()
    traduccion = input(f"Ingrese la traducción de '{palabra}' en inglés: ").lower()
    traducciones[palabra] = traduccion
    continuar = input("¿Quieres agregar otra palabra? (s/n): ")

# Imprimir las traducciones
print("\nDiccionario de traducciones:")
for espanol, ingles in traducciones.items():
    print(f"{espanol}: {ingles}")
