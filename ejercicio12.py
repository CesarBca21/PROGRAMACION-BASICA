# Registro de estudiantes con notas y asignaturas
estudiantes = {}

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Ingresa el nombre del estudiante: ")
    asignaturas = {}
    
    continuar_asignatura = "s"
    while continuar_asignatura.lower() == "s":
        asignatura = input("Ingrese el nombre de la asignatura: ")
        nota = int(input(f"Ingrese la calificación en {asignatura}: "))
        asignaturas[asignatura] = nota
        continuar_asignatura = input("¿Quieres agregar otra asignatura? (s/n): ")
    
    amigos = input("Ingresa los nombres de los amigos, separados por comas: ").split(",")
    amigos = [amigo.strip() for amigo in amigos]
    
    estudiantes[nombre] = {"asignaturas": asignaturas, "amigos": amigos}
    continuar = input("¿Quieres agregar otro estudiante? (s/n): ")

# Imprimir los datos de los estudiantes
print("\nRegistro de estudiantes:")
for nombre, info in estudiantes.items():
    print(f"Estudiante: {nombre}")
    print(f"  Asignaturas y calificaciones: {info['asignaturas']}")
    print(f"  Amigos: {info['amigos']}")
