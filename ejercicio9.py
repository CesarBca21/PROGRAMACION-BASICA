import math

# Función para calcular la distancia de un punto al origen
def distancia_al_origen(punto):
    x, y = punto
    return math.sqrt(x**2 + y**2)

# Lista de puntos en el plano
puntos = [(1, 2), (3, 4), (0, 1), (-1, -1), (2, 3)]

# Ordenar los puntos por su distancia al origen
puntos_ordenados = sorted(puntos, key=distancia_al_origen)

# Imprimir los puntos ordenados
print("Puntos ordenados por su distancia al origen:")
for punto in puntos_ordenados:
    print(punto)
