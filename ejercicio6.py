# Diccionario de notas de estudiantes
notas_estudiantes = {}

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Ingresa el nombre del estudiante: ")
    notas = input(f"Ingrese las calificaciones de {nombre}, separadas por comas: ").split(",")
    # Convertimos las notas a enteros
    notas = [int(nota) for nota in notas]
    notas_estudiantes[nombre] = notas
    continuar = input("¿Quieres agregar otro estudiante? (s/n): ")

# Imprimir las notas de los estudiantes
for estudiante, calificaciones in notas_estudiantes.items():
    print(f"{estudiante}: {calificaciones}")
