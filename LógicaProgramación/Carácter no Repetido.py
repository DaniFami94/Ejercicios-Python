#Dado un string, encuentra el primer carácter que no se repite y devuelve su posición. Si todos los caracteres están repetidos, devuelve una indicación de que no existe tal carácter.


def calculateCaracter(string):
    # Diccionario para almacenar las frecuencias de los caracteres
    letters = {}
    
    # Primera pasada: contar las ocurrencias de cada carácter
    for i in range(len(string)):
        currentCaracter = string[i]  # Carácter actual
        if currentCaracter in letters:
            letters[currentCaracter] += 1  # Incrementa el contador
        else:
            letters[currentCaracter] = 1  # Inicializa el contador en 1

    # Segunda pasada: encontrar el primer carácter no repetido
    for i in range(len(string)):
        if letters[string[i]] == 1:
            return f"El primer carácter no repetido es '{string[i]}' en la posición {i}"
    
    # Si no hay caracteres no repetidos
    return "No hay caracteres no repetidos"

# Ejemplo de uso
result = calculateCaracter("aabbc")
print(result)  # Resultado esperado: "El primer carácter no repetido es 'c' en la posición 4"
