#Solo puedes moverte hacia la derecha o hacia abajo,debes calcular el nivel total de peligro de camino más seguro.

#La pesadilla esta representada por una matriz de tamaño n x m, tienes que devolver el valor total de peligro del camino más seguro.

def findSafestPath(dream):
 rowsNum = len(dream)
 colomnsNum = len(dream[0])

 dangerLevels = []
 dangerLevels[0] = dream[0][0] #guardamos la posición inicial, que seria la esquina superior izquierda
 for col in range(1,colomnsNum): #iniciamos el bucle en valor 1
  dangerLevels[col] = dangerLevels[col - 1] + dream[0][col] # acumulamos el valor de dangerLevels
  
    
    
 return rowsNum , colomnsNum




dream = [[1,3,1],
         [1,5,1],
         [4,2,1],]

print(findSafestPath(dream))