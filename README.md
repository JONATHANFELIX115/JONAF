# Función para calcular el promedio de temperaturas de varias ciudades durante varias semanas
def calcular_temperaturas_promedio(temperaturas):
    """
    Esta función recibe un diccionario con las temperaturas semanales de varias ciudades.
    Calcula y retorna el promedio de temperaturas de cada ciudad.
    
    :param temperaturas: Un diccionario donde las claves son los nombres de las ciudades
                         y los valores son listas de temperaturas por semana (listas de números).
                         Ejemplo: {'Quito': [14.5, 15.3, 13.8, 14.1], ...}
                         
    :return: Un diccionario donde las claves son los nombres de las ciudades y los valores
             son el promedio de temperaturas para cada ciudad. Ejemplo: {'Quito': 14.43, ...}
    """
    # Crear un diccionario vacío para almacenar los promedios
    promedios = {}
    
    # Iterar sobre cada ciudad en el diccionario de temperaturas
    for ciudad, temps in temperaturas.items():
        # Sumar todas las temperaturas de la ciudad y dividir entre la cantidad de temperaturas
        promedio = sum(temps) / len(temps)
        # Guardar el promedio en el diccionario promedios, utilizando la ciudad como clave
        promedios[ciudad] = promedio
    
    # Devolver el diccionario que contiene los promedios de cada ciudad
    return promedios

# Datos de ejemplo: Quito, Babahoyo y Puyo con sus temperaturas durante 4 semanas
temperaturas_ciudades = {
    'Quito': [14.5, 15.3, 13.8, 14.1],  # Temperaturas en °C durante 4 semanas
    'Babahoyo': [26.2, 27.0, 26.5, 26.8],  # Temperaturas en °C durante 4 semanas
    'Puyo': [22.4, 21.9, 22.8, 23.1]  # Temperaturas en °C durante 4 semanas
}

# Llamar a la función para calcular los promedios de temperatura
promedios = calcular_temperaturas_promedio(temperaturas_ciudades)

# Imprimir los resultados: el promedio de temperatura para cada ciudad
for ciudad, promedio in promedios.items():
    # Mostrar el promedio de temperatura redondeado a 2 decimales
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")
