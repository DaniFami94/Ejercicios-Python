"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""


def es_primo(n):
    # Caso especial: Si el número es menor o igual a 1, no es primo
    if n <= 1:
        return False

    # Verificar si el número es divisible por algún número desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Si encontramos un divisor, no es primo

    return True  # Si no encontramos divisores, es primo


# Bucle para imprimir los números primos entre 1 y 100
for i in range(1, 101):
    if es_primo(i):
        print(i, "Es primo")
    else:
        print(i, "No es primo")

