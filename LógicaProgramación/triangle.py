"""Give an integer n, representing the height.
Draw a triangle

ex) n = 5

*****
 ****
  ***
   **
    *
"""


def triangle(numero):
    for i in range(numero):
        numero = numero - 1
        print(i * " " + numero * "* ")


triangle(5)
