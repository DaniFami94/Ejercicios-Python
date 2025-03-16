"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""

def es_anagrama(palabra1, palabra2):
    # Normalizar las palabras (convertir a minúsculas y eliminar espacios)
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    if palabra1 == palabra2:
        return False
    # Comparar las palabras ordenando los caracteres
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
print(es_anagrama("amor", "roma"))  # Debería devolver True
print(es_anagrama("amor", "ramo"))  # Debería devolver True
print(es_anagrama("amor", "amor"))  # Debería devolver False