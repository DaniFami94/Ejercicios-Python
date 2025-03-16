from Personaje import Personaje
from Guerrero import Guerrero
from Mago import Mago
from Arena import Arena
from Acciones import Acciones

if __name__ == "__main__":
    goku = Personaje("Goku", 150, 20, 100, 5)
    hercules = Guerrero("Hercules", 100, 10, 100, 3, 5)
    sauron = Mago("Sauron", 50, 30, 80, 2, 5)

    # Crear la arena y ejecutar el combate
    arena = Arena()
    arena.combate(hercules, sauron)

    # Ejemplo de otras acciones disponibles
    # Acciones.subir_nivel(hercules, 10, 5, 20, 2)
    # Acciones.cambiar_arma(hercules)
    # Acciones.cambiar_magia(sauron)
