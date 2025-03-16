"""
Escribe una función que tome una lista de números y determine si está ordenada de forma ascendente.

Requisitos:

No puedes usar funciones propias del lenguaje como sorted().

La función debe devolver True si la lista está ordenada en orden ascendente, y False en caso contrario.

Si la lista está vacía o tiene un solo elemento, se considera ordenada. """

numeros = [5, 3, 2, 1]


def listaOrdenada(numeros):

    # una lista vacio con un solo elemento esta ordenada
    if len(numeros) <= 1:
        return True

    # Recorremos la lista comparando elementos consecutivos

    for i in range(len(numeros) - 1): #  necesitamos recorrer la lista solo hasta el penúltimo elemento, es decir, no necesitamos comprobar el último elemento con el siguiente, porque no existe un "siguiente". Por eso usamos len(numeros) - 1, que es el índice del penúltimo elemento.

        if numeros[i] > numeros[i + 1]:  # si un elemento es mayor que el siguiente

            return False

    return True # Si recorremos todo sin encontrar desorden, está ordenada
"""
Primera iteración:
i = 0: Comparamos numeros[0] (5) con numeros[1] (3).
5 no es menor que 3, por lo que la lista no está ordenada.
El código retorna False inmediatamente y termina. No se necesitan más iteraciones.

"""

print(listaOrdenada(numeros))
