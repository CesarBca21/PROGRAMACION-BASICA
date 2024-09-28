# Agenda de contactos
agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no se encontró.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"El contacto {nombre} no se encontró.")

# Menú básico
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
        agregar_contacto(nombre, telefono)
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
