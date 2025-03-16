
#**Uso de in en un for (Iteración Directa)**
"""
 Las funciones len(), in y range() en Python cumplen diferentes roles cuando se usan en un bucle for. Aquí te explico las diferencias clave:

1. Uso de in en un for (Iteración Directa)
Cuando usas in en un for, iteras directamente sobre los elementos de una lista, cadena, tupla o cualquier iterable.

Ejemplo:
"""
numeros = [10, 20, 30, 40]
for num in numeros:
    print(num)

#Salida: 10,20,30,40
""""
 Ventajas:
- Es más legible y directo.
- No necesitas usar índices manualmente.
- Funciona con cualquier iterable (listas, diccionarios, cadenas, etc.).
"""

#Uso de range(len(iterable)) (Iteración por Índice)
"""Cuando usas range(len(iterable)), iteras a través de los índices en lugar de los elementos directamente.
"""

numeros = [10, 20, 30, 40]
for i in range(len(numeros)):
    print(numeros[i])

#Salida: 10,20,30,40

"""Ventajas:
- Útil cuando necesitas modificar elementos dentro de una lista.
- Permite acceder al índice para hacer operaciones con él.
"""

# Diferencia entre len() y range() en un for

"""
- len(iterable): Solo devuelve la cantidad de elementos en el iterable. No genera números por sí solo.

- range(n): Genera una secuencia de números del 0 a n-1, útil cuando necesitas recorrer listas por índice.
"""

frutas = ["manzana", "banana", "cereza"]

print(len(frutas))  # 3
print(list(range(len(frutas))))  # [0, 1, 2]