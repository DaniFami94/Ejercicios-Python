from Personaje import Personaje


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, magia):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.__magia = magia

    @property
    def magia(self):
        return self.__magia

    @magia.setter
    def magia(self, valor):
        self.__magia = valor

    def cambiar_magia(self):
        opcion = int(
            input("Elige un hechizo: (1) Bola de fuego, daño 8. (2) Rayo, daño 10")
        )
        if opcion == 1:
            self.magia = 8
        elif opcion == 2:
            self.magia = 10
        else:
            print("Número de hechizo incorrecto")

    def atributos(self):
        super().atributos()
        print(".Magia: ", self.__magia)

    def daño(self, enemigo):
        return self.inteligencia * self.magia - enemigo.defensa
