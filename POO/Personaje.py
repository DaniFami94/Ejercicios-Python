# Ejemplo de abstracción
# vamos a volver los atributos privados para que solo se puedan modificar desde la clase Personaje
# El poliformismo nos permite crear funciones que reciban objetos con metodos que tenga el mismo nombre, pero que hagan cosas diferentes, por ejemplo, el metodo atacar de la clase Guerrero y de la clase Personaje, ambos tienen el mismo nombre, pero hacen cosas diferentes, el de Guerrero incluye el daño de la espada, mientras que el de Personaje no, esto es poliformismo, el mismo nombre, pero comportamientos diferentes.


class Personaje:
    """
    Clase base para todos los personajes del juego.

    Attributes:
        __nombre (str): Nombre del personaje
        __fuerza (int): Puntos de fuerza del personaje
        __inteligencia (int): Puntos de inteligencia del personaje
        __vida (int): Puntos de vida del personaje
        __defensa (int): Puntos de defensa del personaje
    """

    def __init__(
        self, nombre: str, fuerza: int, inteligencia: int, vida: int, defensa: int
    ):
        """
        Inicializa un nuevo personaje.

        Args:
            nombre: Nombre del personaje
            fuerza: Puntos de fuerza iniciales
            inteligencia: Puntos de inteligencia iniciales
            vida: Puntos de vida iniciales
            defensa: Puntos de defensa iniciales
        """
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__vida = vida
        self.__defensa = defensa

    # Propiedades (getters y setters)
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del personaje."""
        return self.__nombre

    @property
    def fuerza(self) -> int:
        """Obtiene los puntos de fuerza."""
        return self.__fuerza

    @property
    def inteligencia(self) -> int:
        """Obtiene los puntos de inteligencia."""
        return self.__inteligencia

    @property
    def vida(self) -> int:
        """Obtiene los puntos de vida actuales."""
        return self.__vida

    @vida.setter
    def vida(self, valor: int):
        """
        Establece los puntos de vida.

        Args:
            valor: Nuevos puntos de vida
        """
        self.__vida = valor

    @property
    def defensa(self) -> int:
        """Obtiene los puntos de defensa."""
        return self.__defensa

    # Métodos públicos
    def atributos(self):
        """Muestra todos los atributos del personaje."""
        print(f"{self.__nombre}:")
        print(f".Fuerza: {self.__fuerza}")
        print(f".Inteligencia: {self.__inteligencia}")
        print(f".Vida: {self.__vida}")
        print(f".Defensa: {self.__defensa}")

    def esta_vivo(self) -> bool:
        """
        Verifica si el personaje está vivo.

        Returns:
            bool: True si está vivo, False si no
        """
        return self.__vida > 0

    def daño(self, enemigo) -> int:
        """
        Calcula el daño que este personaje hace a un enemigo.

        Args:
            enemigo: El personaje enemigo que recibirá el daño

        Returns:
            int: Cantidad de daño calculado
        """
        return self.__fuerza - enemigo.defensa

    def subir_nivel(self, fuerza, inteligencia, vida, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__vida += vida
        self.__defensa += defensa

    # Volvemos morir privado para que no se pueda acceder desde fuera de la clase y este sea solo gestionando y llamado por el metodo atacar
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(
            self.__nombre,
            "ha atacado a",
            enemigo.__nombre,
            "y le ha infligido",
            daño,
            "puntos de daño",
            "la vida del enemigo es de",
            enemigo.__vida,
            "puntos",
        )
        if enemigo.esta_vivo():

            print("la vida del enemigo es de", enemigo.__vida, "puntos")

        else:

            enemigo.__morir()

    # si queremos acceder o modificar los atributos privados individualmente, podemos hacerlo mediante un metodo get y set

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("La fuerza no puede ser negativa")
        else:
            self.__fuerza = fuerza


# Declaramos los objetos de la clase
# mi_personaje = Personaje("Daniel", 150, 15, 100, 3)
# mi_enemigo = Personaje("Enemigo", 10, 15, 100, 3)

# # Llamamos a los metodos de la clase
# # mi_personaje.atributos()
# # mi_personaje.subir_nivel(2, 1, 10, 1)
# # mi_personaje.atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.set_fuerza(-5)
# mi_personaje.atributos()
