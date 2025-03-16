# El poliformismo nos permite crear funciones que reciban objetos con metodos que tengan el mismo nombre y así ejecutar acciones diferentes según la clase de  ese objeto.
# Además de que nos permite reutilizar código, ya que podemos crear funciones que reciban objetos de diferentes clases y ejecuten acciones diferentes según la clase del objeto.


class Cafe:
    def que_soy(self):
        print("Soy un café")


class Te:
    def que_soy(self):
        print("Soy un te")


def definicion_bebida(bebida):
    bebida.que_soy()


# el metodo que_soy tomara multiples formas en función al objeto que reciba

definicion_bebida(Cafe())
definicion_bebida(Te())
