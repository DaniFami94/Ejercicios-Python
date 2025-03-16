""""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 """


def reverseString (word):

 newWord = ""

 for char in range(len(word)):
  # Agrega el carácter actual al inicio de newWord
  newWord = word[char] + newWord
  

 return newWord





print(reverseString("hola mundo"))