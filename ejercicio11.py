# Registro de compras en una tienda
compras = []
total_gastado = 0

continuar = "s"
while continuar.lower() == "s":
    producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad comprada de {producto}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
    compras.append((producto, cantidad, precio_unitario))
    total_gastado += cantidad * precio_unitario
    continuar = input("¿Quieres agregar otra compra? (s/n): ")

# Imprimir las compras y el total gastado
print("\nCompras realizadas:")
for producto, cantidad, precio in compras:
    print(f"Producto: {producto}, Cantidad: {cantidad}, Precio unitario: ${precio:.2f}")

print(f"\nTotal gastado: ${total_gastado:.2f}")
