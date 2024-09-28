# Registro de ventas por producto y mes
ventas = []

continuar = "s"
while continuar.lower() == "s":
    producto = input("Ingresa el nombre del producto: ")
    mes = input("Ingresa el mes de la venta: ")
    cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto}: "))
    ventas.append({"producto": producto, "mes": mes, "cantidad_vendida": cantidad_vendida})
    continuar = input("¿Quieres agregar otra venta? (s/n): ")

# Imprimir el registro de ventas
print("\nRegistro de ventas:")
for venta in ventas:
    print(f"Producto: {venta['producto']}, Mes: {venta['mes']}, Cantidad vendida: {venta['cantidad_vendida']}")
