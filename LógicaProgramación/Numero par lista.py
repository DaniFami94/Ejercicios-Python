# Dada una lista de números, escribe un programa que devuelva una nueva lista con solo los números pares de la lista original.

numeros = [1, 2, 3, 4, 5, 6]



def calcularPares(numeros):
 
 lista = []
 
 for i in numeros:
        if i % 2 == 0:
         lista.append(i)

 return lista



print(calcularPares(numeros))