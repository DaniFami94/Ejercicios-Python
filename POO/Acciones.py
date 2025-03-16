class Acciones:
    @staticmethod
    def atacar(atacante, defensor):
        daño = atacante.daño(defensor)
        defensor.vida = defensor.vida - daño
        print(
            atacante.nombre,
            "ha atacado a",
            defensor.nombre,
            "y le ha infligido",
            daño,
            "puntos de daño",
        )

        if defensor.esta_vivo():
            print("La vida de", defensor.nombre, "es de", defensor.vida, "puntos")
        else:
            Acciones.morir(defensor)

    @staticmethod
    def morir(personaje):
        personaje.vida = 0
        print(personaje.nombre, "ha muerto")

    @staticmethod
    def subir_nivel(personaje, fuerza, inteligencia, vida, defensa):
        personaje.fuerza += fuerza
        personaje.inteligencia += inteligencia
        personaje.vida += vida
        personaje.defensa += defensa
        print(personaje.nombre, "ha subido de nivel!")

    @staticmethod
    def cambiar_arma(guerrero):
        opcion = int(
            input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10")
        )
        if opcion == 1:
            guerrero.espada = 8
            print(guerrero.nombre, "ahora usa Acero Valyrio")
        elif opcion == 2:
            guerrero.espada = 10
            print(guerrero.nombre, "ahora usa Matadragones")
        else:
            print("Número de arma incorrecto")

    @staticmethod
    def cambiar_magia(mago):
        opcion = int(
            input("Elige un hechizo: (1) Bola de fuego, daño 8. (2) Rayo, daño 10")
        )
        if opcion == 1:
            mago.magia = 8
            print(mago.nombre, "ahora usa Bola de fuego")
        elif opcion == 2:
            mago.magia = 10
            print(mago.nombre, "ahora usa Rayo")
        else:
            print("Número de hechizo incorrecto")
