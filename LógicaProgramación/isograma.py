def esIsograma(palabra):
 
 listaDeLetras = [] # Lista vacía
 palabra = palabra.lower() # Convertimos la palabra a minúsculas

 match(palabra):
   
   case "":
     print("La palabra está vacía")
     return False
   
   case palabra.isalpha():
     print("La palabra contiene números")
     return False
   
   case palabra.isalnum():
     print("La palabra contiene caracteres especiales")
     return False
   
   case " ":
     print("La palabra contiene espacios")
     return False
     
 
 for letra in palabra: # Recorremos la palabra
  
    if letra in listaDeLetras: # Si la letra ya está en la lista
     
     print(palabra + " no es Isograma")
     
     return False
    
    listaDeLetras.append(letra) # Si no cae en el if, añadimos la letra a la lista hasta iterar toda la palabra

 print(palabra + " es Isograma")  
 
 return True # Si no se repiten letras, es Isograma
  
esIsograma("hola m")



