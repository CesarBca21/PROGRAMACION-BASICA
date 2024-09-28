# Agenda de contactos mejorada con diccionarios
agenda = []

def agregar_contacto(nombre, telefono, correos):
    agenda.append({"nombre": nombre, "telefono": telefono, "correos": correos})
    print(f"Contacto {nombre} agregado.")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correos: {', '.join(contacto['correos'])}")
            return
    print(f"El contacto {nombre} no se encontró.")

def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print(f"El contacto {nombre} no se encontró.")

# Menú
while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el número de teléfono: ")
        correos = input("Ingresa los correos electrónicos, separados por comas: ").split(",")
        correos = [correo.strip() for correo in correos]
        agregar_contacto(nombre, telefono, correos)
    elif opcion == "2":
        nombre = input("Ingresa el nombre a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        nombre = input("Ingresa el nombre a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
