"""Dado un string que contiene únicamente los caracteres (, ), {, }, [ y ], escribe una función que determine si la secuencia de paréntesis está balanceada."""
def parentesisBalanceado(parentesis):
    pila = []  # Lista para almacenar los paréntesis de apertura.

    for char in parentesis:
        # Si encontramos un paréntesis de apertura, lo agregamos a la pila.
        if char == "(" or char == "{" or char == "[":
            pila.append(char)
        # Si encontramos un paréntesis de cierre, verificamos que coincida con el último de la pila.
        elif char == ")" or char == "}" or char == "]":
            if not pila:
                return False  # Si la pila está vacía, significa que no hay paréntesis de apertura para cerrar.
            
            last_open = pila.pop()  # Sacamos el último paréntesis abierto.
            
            # Verificamos que el paréntesis de cierre coincida con el último paréntesis abierto.
            if char == ")" and last_open != "(":
                return False
            elif char == "}" and last_open != "{":
                return False
            elif char == "]" and last_open != "[":
                return False

    # Si la pila está vacía al final, todos los paréntesis están balanceados.
    return len(pila) == 0

# Pruebas
print(parentesisBalanceado("({[]})"))  # True
print(parentesisBalanceado("([{})"))   # False
print(parentesisBalanceado("()"))      # True
print(parentesisBalanceado("{[()]}"))  # True
print(parentesisBalanceado("{[(])}"))  # False
