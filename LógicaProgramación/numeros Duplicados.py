numeros = [0, 0, 1, 2, 3, 4, 5, 6, 5]

def duplicado(numeros):
    vistos = []  # Lista para números ya encontrados
    repetidos = []  # Lista para números duplicados

    for num in numeros:
        print("Numero actual:", num)
        
        if num in vistos:  # Si el número ya está en vistos
            print(f"{num} ya fue visto")
            if num not in repetidos:  # Si aún no está en repetidos
                repetidos.append(num)  # Lo agregamos a repetidos
        else:
            vistos.append(num)  # Si no está en vistos, lo agregamos

    return repetidos  # Devolvemos la lista de números duplicados

print(duplicado(numeros))  # Esto debería imprimir [0, 5]