# Registro de alumnos con tuplas
alumnos = []

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Ingresa el nombre del alumno: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    calificaciones = input(f"Ingrese las calificaciones de {nombre}, separadas por comas: ").split(",")
    calificaciones = [int(nota) for nota in calificaciones]
    alumnos.append((nombre, edad, calificaciones))
    continuar = input("¿Quieres agregar otro alumno? (s/n): ")

# Imprimir la lista de alumnos y sus datos
print("\nLista de alumnos:")
for alumno in alumnos:
    nombre, edad, calificaciones = alumno
    print(f"Nombre: {nombre}, Edad: {edad}, Calificaciones: {calificaciones}")
