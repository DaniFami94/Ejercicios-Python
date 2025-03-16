from Acciones import Acciones


class Arena:
    def __init__(self):
        self.MAX_TURNOS = 50

    def combate(self, jugador_1, jugador_2):
        turno = 0

        while (
            jugador_1.esta_vivo() and jugador_2.esta_vivo() and turno < self.MAX_TURNOS
        ):
            print("\nTurno", turno)

            print(">>> Acción de ", jugador_1.nombre, ":", sep="")
            Acciones.atacar(jugador_1, jugador_2)
            jugador_2.atributos()

            if not jugador_2.esta_vivo():
                break

            print(">>> Acción de ", jugador_2.nombre, ":", sep="")
            Acciones.atacar(jugador_2, jugador_1)
            jugador_1.atributos()

            turno += 1

        if turno >= self.MAX_TURNOS:
            print("\nEl combate ha terminado en empate por límite de turnos")
        elif jugador_1.esta_vivo():
            print("\nHa ganado", jugador_1.nombre)
        else:
            print("\nHa ganado", jugador_2.nombre)
