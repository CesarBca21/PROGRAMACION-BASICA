# Diccionario de sinónimos
sinonimos = {
    "rápido": "veloz",
    "feliz": "contento",
    "grande": "enorme",
    "inteligente": "listo"
}

palabra = input("Ingresa una palabra para buscar su sinónimo: ").lower()

if palabra in sinonimos:
    print(f"El sinónimo de {palabra} es {sinonimos[palabra]}.")
else:
    print(f"No se encontró un sinónimo para la palabra '{palabra}'.")

# Imprimir solo las claves del diccionario
print("\nPalabras en el diccionario:")
for clave in sinonimos.keys():
    print(clave)
