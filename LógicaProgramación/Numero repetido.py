# Dada una lista de números, escribe un programa que cuente cuántas veces aparece un número específico en la lista.


nums = [3, 6, 8, 2, 6, 6, 6]

def numRepetido(nums):
 target = 6
 newIndex = 0
 
 for i in (nums):
   if i == target:
    newIndex = newIndex + 1
 return "el número se repite " + str(newIndex) + " veces"




print(numRepetido(nums))