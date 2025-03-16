"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 """
import math

cuadrado = [6,6]

def calcularAreaPoligono(cuadrado):
 area = 0  
 lado = cuadrado[0]
 area = lado * lado
    
 return area

print("El area del cuadrado es",calcularAreaPoligono(cuadrado))


# Lista de valores del triángulo: [base, lado, lado]
triangulo = [12, 16, 16]

def calcularAreaPoligono(triangulo):
    # Asignamos los valores de la base y los lados
    base = triangulo[0]
    lado = triangulo[1]

    # Calculamos la altura usando el teorema de Pitágoras
    # altura = sqrt(lado^2 - (base/2)^2)
    altura = math.sqrt(lado**2 - (base / 2)**2)

    # Calculamos el área del triángulo
    # Área = (base * altura) / 2
    area = (base * altura) / 2

    return area

# Llamamos a la función y mostramos el resultado
print("El área del triángulo isósceles es:", calcularAreaPoligono(triangulo))


rectangulo = [6,4]

def calcularAreaPoligono(rectangulo):
  base = rectangulo[0]
  altura = rectangulo[1] 
 
  area = base * altura
    
  return area

print("El area del rectangulo es",calcularAreaPoligono(rectangulo))

