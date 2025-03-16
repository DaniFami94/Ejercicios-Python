#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

def createMagicPotion(potions, target):
    # Creamos un diccionario vacío llamado `seen` para almacenar cada poción y su índice
    seen = {}

    # Empezamos un bucle que recorre cada índice `i` en la lista `potions`
    for i in range(len(potions)):
        # `currentPotion` obtiene el valor de la poción actual en la posición `i`
        currentPotion = potions[i]
        print(currentPotion)  # Imprimimos el valor de la poción actual para verificar su valor

        # Calculamos el complemento de `currentPotion`, es decir,
        # el valor que necesitamos encontrar en `seen` para que la suma sea igual a `target`
        complement = target - currentPotion
        print({complement})  # Imprimimos el valor del complemento para verificar

        # Verificamos si `complement` ya está en el diccionario `seen`
        if complement in seen:
            # Si `complement` está en `seen`, significa que hemos encontrado dos pociones
            # que suman `target`. Retornamos una lista con los índices de ambas pociones
            return [seen[complement], i]

        # Si `complement` no está en `seen`, añadimos `currentPotion` al diccionario `seen`
        # usando su valor como clave y su índice `i` como valor
        seen[currentPotion] = i

    # Si terminamos el bucle y no encontramos dos pociones que sumen `target`,
    # retornamos `None` para indicar que no hay tal par de pociones
    return None

# Definimos la lista `potions` y el valor `target`
potions = [4, 5, 6, 2]
target = 8

# Llamamos a `createMagicPotion` con `potions` y `target` y mostramos el resultado
print(createMagicPotion(potions, target))
