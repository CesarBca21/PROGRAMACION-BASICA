# Diccionario de películas con géneros y actores
peliculas = {}

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Ingresa el nombre de la película: ")
    generos = input("Ingresa los géneros de la película, separados por comas: ").split(",")
    generos = [genero.strip() for genero in generos]
    
    actores = input("Ingresa los nombres de los actores principales, separados por comas: ").split(",")
    actores = [actor.strip() for actor in actores]
    
    peliculas[nombre] = {"géneros": generos, "actores": actores}
    continuar = input("¿Quieres agregar otra película? (s/n): ")

# Imprimir el diccionario de películas
print("\nPelículas registradas:")
for pelicula, info in peliculas.items():
    print(f"Película: {pelicula}")
    print(f"  Géneros: {', '.join(info['géneros'])}")
    print(f"  Actores: {', '.join(info['actores'])}")
