lista = [3, 6, 8, 2, 6]

def mayor(lista):
    max_value = lista[0]  # Inicializamos max_value con el primer elemento de la lista
    for i in lista:       # Recorremos cada número en la lista
        if i > max_value:  # Si el número actual es mayor que el máximo
            max_value = i   # Actualizamos el máximo
    return max_value   # Devolvemos el máximo encontrado

# Llamada a la función y mostrar el resultado
print(mayor(lista))  # Debería devolver 8




