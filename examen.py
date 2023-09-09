# Diccionario 
    calificaciones = {
        'juan': [90, 85, 88, 92, 78],
        'maria': [76, 89, 91, 84, 72],
        'pedro': [87, 82, 80, 78, 95]
    }

    # Función para calcular el promedio de un estudiante con argumento  con def que  es una palabra reservada que indica a Python que una nueva función está siendo definida
    def calcular_promedio(calificaciones_estudiante):
        # Calcula la suma de las calificaciones y luego divide por la cantidad de calificaciones con dos funciones reservadas en python
        return sum(calificaciones_estudiante) / len(calificaciones_estudiante)

    # Calcula y muestra el promedio de cada estudiante
    for estudiante, calificaciones_estudiante in calificaciones.items():
        # Llama a la función calcular_promedio con las calificaciones del estudiante actual
        promedio = calcular_promedio(calificaciones_estudiante)
        # Muestra el nombre del estudiante y su promedio
        print('El promedio de ', estudiante, 'es:', promedio)