# Diccionario de países con información geográfica
paises = {}

continuar = "s"
while continuar.lower() == "s":
    pais = input("Ingresa el nombre del país: ")
    
    # Lista de ciudades importantes
    ciudades = input(f"Ingrese las ciudades importantes de {pais}, separadas por comas: ").split(",")
    ciudades = [ciudad.strip() for ciudad in ciudades]
    
    # Lista de coordenadas (latitud y longitud)
    coordenadas = []
    for ciudad in ciudades:
        print(f"Ingrese las coordenadas de {ciudad}:")
        latitud = float(input("  Latitud: "))
        longitud = float(input("  Longitud: "))
        coordenadas.append({"ciudad": ciudad, "latitud": latitud, "longitud": longitud})
    
    paises[pais] = {"ciudades_importantes": ciudades, "coordenadas": coordenadas}
    continuar = input("¿Quieres agregar otro país? (s/n): ")

# Imprimir la información geográfica de los países
print("\nInformación geográfica de los países:")
for pais, info in paises.items():
    print(f"\nPaís: {pais}")
    print(f"  Ciudades importantes: {', '.join(info['ciudades_importantes'])}")
    print("  Coordenadas:")
    for coord in info['coordenadas']:
        print(f"    Ciudad: {coord['ciudad']}, Latitud: {coord['latitud']}, Longitud: {coord['longitud']}")
