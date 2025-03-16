# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
# usar // hace que la division sea sin decimales, siempre devolverá un número entero
#  */


def getBinario():
    n = 13
    binario = []

    while n > 0:

        residuo = n % 2
        n = n // 2
        binario.append(str(residuo))
    binario.reverse()

    print("".join(binario))  # Convierte la lista a una cadena y la imprime


getBinario()
