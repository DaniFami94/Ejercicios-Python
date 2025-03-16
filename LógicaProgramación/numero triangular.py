# Este programa determina si un número es triangular o no. Un número es triangular si es la suma de los primeros n números naturales. Por ejemplo, 6 es triangular porque 6 = 1 + 2 + 3.


def is_triangular(t):

    level = 1  # declaramos una variable level que va a ser el nivel de la piramide

    while t > 0:
        t = t - level  # restamos el nivel a t
        level = level + 1  # aumentamos el nivel 1
    if t == 0:
        return "El numero es triangular"
    else:
        return "el numero no es triangular"


print(is_triangular(6))
