numeros = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5]


def numeroUnico(numeros):
    # Diccionario para contar las apariciones de cada número
    conteo = {}

    # Primera pasada: contar las apariciones
    for num in numeros:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1

    # Segunda pasada: encontrar el número que aparece solo una vez
    for num in numeros:
        if conteo[num] == 1:
            return f"El número único es {num}"

    return "No hay números únicos"


print(numeroUnico(numeros))
