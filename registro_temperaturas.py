# Importamos la librería numpy para manejar los cálculos si es necesario
import numpy as np

# Definimos una lista con los nombres de las ciudades
ciudades = ["CiudadA", "CiudadB", "CiudadC"]

# Creamos una matriz 3D donde cada ciudad tendrá 7 días y 4 semanas
# Utilizamos valores aleatorios de temperatura entre 15 y 35 grados para simular los datos
temperaturas = np.random.randint(15, 35, (len(ciudades), 7, 4))

# Visualizamos la estructura de la matriz
print("Matriz 3D de temperaturas por ciudad, día y semana:")
print(temperaturas)
# Recorremos cada ciudad
for i in range(len(ciudades)):
    print(f"\nPromedios de temperatura para {ciudades[i]}:")

    # Recorremos cada semana
    for semana in range(4):  # Hay 4 semanas
        suma_temperaturas = 0

        # Recorremos cada día de la semana (7 días)
        for dia in range(7):
            suma_temperaturas += temperaturas[i][dia][semana]

        # Calculamos el promedio de la semana
        promedio_semanal = suma_temperaturas / 7
        print(f"  Semana {semana + 1}: {promedio_semanal:.2f}°C")
Promedios de temperatura para CiudadA:
  Semana 1: 23.43°C
  Semana 2: 25.57°C
  Semana 3: 22.86°C
  Semana 4: 24.14°C

Promedios de temperatura para CiudadB:
  Semana 1: 21.29°C
  Semana 2: 23.00°C
  Semana 3: 22.43°C
  Semana 4: 26.57°C

Promedios de temperatura para CiudadC:
  Semana 1: 24.00°C
  Semana 2: 26.86°C
  Semana 3: 25.43°C
  Semana 4: 22.57°C


# Función para calcular el promedio de temperaturas de varias ciudades durante varias semanas
def calcular_temperaturas_promedio(temperaturas):
    """
    Esta función recibe un diccionario con las temperaturas semanales de varias ciudades.
    Calcula y retorna el promedio de temperaturas de cada ciudad.

    :param temperaturas: diccionario {ciudad: [lista de temperaturas por semana]}
    :return: diccionario con el promedio de temperatura por ciudad
    """
    promedios = {}

    # Recorremos cada ciudad y sus temperaturas semanales
    for ciudad, temps in temperaturas.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio

    return promedios


# Datos de ejemplo: Quito, Babahoyo y Puyo, con temperaturas durante 4 semanas
temperaturas_ciudades = {
    'Quito': [14.5, 15.3, 13.8, 14.1],  # Temperaturas en °C para 4 semanas
    'Babahoyo': [26.2, 27.0, 26.5, 26.8],
    'Puyo': [22.4, 21.9, 22.8, 23.1]
}

# Calcular promedios
promedios = calcular_temperaturas_promedio(temperaturas_ciudades)

# Imprimir resultados
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")


