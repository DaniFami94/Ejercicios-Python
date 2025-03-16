"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""

def fibonacci(n):
    # Paso 1: Inicializar la lista con los dos primeros números de la secuencia.
    secuencia = [0, 1]

    # Paso 2: Comprobar si n es menor o igual a 0
    if n <= 0:
        return []  # Si no se quiere ningún término, devolver una lista vacía
    elif n == 1:
        return [0]  # Si se quiere solo el primer término, devolver solo [0]

    # Paso 3: Calcular el resto de la secuencia
    for i in range(2, n):  # Comenzar desde el índice 2 hasta n-1
        siguiente = secuencia[i - 1] + secuencia[i - 2]  # Sumar los dos últimos números
        secuencia.append(siguiente)  # Agregar el nuevo número a la lista

    return secuencia  # Devolver la secuencia completa


# Ejemplo de uso
n = 50  # Por ejemplo, queremos los primeros 50 números de Fibonacci
print(fibonacci(n))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]