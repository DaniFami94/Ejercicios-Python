# Problema: Ordenar una lista de números sin usar funciones incorporadas de ordenamiento
# Selection Sort
lista = [5, 2, 9, 1, 5, 6]

def ordenarLista(lista):
    # Recorremos los índices de la lista
    for i in range(len(lista)):
        # Suponemos que el índice actual tiene el valor mínimo
        min_index = i

        # Recorremos los elementos posteriores al índice actual
        for j in range(i + 1, len(lista)):
            # Si encontramos un valor menor, actualizamos min_index
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambiamos los valores usando una variable temporal
        valor_temporal = lista[i]               # Guardar el valor actual
        lista[i] = lista[min_index]   # Asignar el valor del índice mínimo
        lista[min_index] = valor_temporal      # Asignar el valor temporal al índice mínimo

    return lista

# Prueba la función
print(ordenarLista(lista))
