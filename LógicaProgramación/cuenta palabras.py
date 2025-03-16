"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 """

def cuentaPalabras(texto):
    # Paso 1: Limpiar el texto
    texto_limpio = ""
    for char in texto:
        # Mantén solo letras y espacios, ignora signos de puntuación
        if char.isalnum() or char.isspace():
            texto_limpio += char.lower()  # Convertimos todo a minúsculas

    # Paso 2: Separar palabras manualmente
    palabras = []
    palabra_actual = ""
    for char in texto_limpio:
        if char.isspace():  # Si encontramos un espacio, añadimos la palabra actual
            if palabra_actual:  # Evitamos añadir cadenas vacías
                palabras.append(palabra_actual)
                palabra_actual = ""  # Reseteamos para la siguiente palabra
        else:
            palabra_actual += char  # Construimos la palabra carácter por carácter
    if palabra_actual:  # Añadimos la última palabra si existe
        palabras.append(palabra_actual)

    # Paso 3: Contar palabras
    contador = {}
    for palabra in palabras:
        if palabra in contador:  # Si la palabra ya está en el diccionario, incrementamos su contador
            contador[palabra] += 1
        else:
            contador[palabra] = 1  # Si no está, la inicializamos con 1

    return contador


# Ejemplo de uso
print(cuentaPalabras("hola me llamo daniel y siempre me dices hola de vuelta"))
