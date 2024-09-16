
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



