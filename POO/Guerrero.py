from Personaje import Personaje

# la funciónsuper() nos permite llamar a los atributos y metodos de la clase padre sin tener que escribirla directamente


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, espada):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.__espada = espada

    @property
    def espada(self):
        return self.__espada

    @espada.setter
    def espada(self, valor):
        self.__espada = valor

    def cambiar_arma(self):
        opcion = int(
            input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10")
        )
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecto")

    # Sobreescribimos el método atributos, para incluir la espada
    def atributos(self):
        super().atributos()
        print(".Espada: ", self.__espada)

    # Sobreescribimos el metodo daño, para agregar el daño de la espada
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


# Creamos al guerrero y vemos sus atributos
hercules = Guerrero("Hercules", 100, 10, 100, 3, "Espada")
hercules.atributos()
hercules.cambiar_arma()
print(hercules.espada)

enemigo = Personaje("Hidra", 50, 20, 80, 2)
hercules.atacar(enemigo)
