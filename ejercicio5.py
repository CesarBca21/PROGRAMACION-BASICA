# Diccionario de precios de productos
precios = {
    "manzana": 1.20,
    "banana": 0.50,
    "naranja": 0.80,
    "pera": 1.50
}

producto = input("Ingresa el nombre del producto para ver su precio: ").lower()

if producto in precios:
    print(f"El precio de {producto} es ${precios[producto]:.2f}.")
else:
    print(f"No se encontró el precio de {producto}.")
