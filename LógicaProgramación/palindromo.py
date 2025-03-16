def isPalindrome(string):
    # Inicializamos un string limpio
    cleaned_string = ""

    # Iteramos sobre cada carácter del string
    for char in string:
        if char.isalnum():  # Verifica si el carácter es alfanumérico
            cleaned_string = cleaned_string + char.lower()  # Convierte a minúscula y lo agrega al string limpio

    # Verifica si el string limpio es igual a su reverso
    if cleaned_string == cleaned_string[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"
# Ejemplo de uso
print(isPalindrome("anita lava la tina"))  # Salida: Es un palíndromo
print(isPalindrome("Hola mundo"))         # Salida: No es un palíndromo
print(isPalindrome("A man a plan a canal Panama"))  # Salida: Es un palíndromo