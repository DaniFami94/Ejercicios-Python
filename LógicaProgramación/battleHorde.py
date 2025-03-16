""" Dadas dos cadenas de texto zombies y humans, donde cada digito (del  al 9) representa el poder de ataque de un combatiente,determina quien queda al final y con cuanto poder de ataque.
importante: las dos cadenas siempre tendran la misma longitud
la salida: es una cadena de texto que representa el resultado final de la batalla """

def battleHorde(zombies, humans):
    z = 0  
    h = 0
    
    # Sumar los poderes de ataque de zombies y humanos
    for i in range(len(zombies)):
        z += int(zombies[i])  # Convierte el dígito en entero antes de sumarlo
        h += int(humans[i])
    
    diff = abs(z - h)
    
    # Determinar el ganador
    if diff == 0:
        return "Empate"

    if h > z:
        return f"Ganan los humanos con una diferencia de poder de ataque de:{diff}h"  # Humanos ganan
    else:
        return f"Ganan los zombies con una diferencia de poder de ataque de:{diff}z"  # Zombies ganan


# Ejemplo
zombies = '242'
humans = '334'


result = battleHorde(zombies, humans)
print(result)  # Salida esperada: "2h"


""" primera ronda: zombie 2 vs human 3 => humano gano (+1)
 segunda ronda: zombie 4 vs human 3+1 => empate
 tercera ronda: zombie 2 vs human 4 => humano gana (+2)
resultado: 2h """


