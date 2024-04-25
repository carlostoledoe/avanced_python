import random
from personaje import Personaje

class Jugador(Personaje):
    
    def ataque(self) -> int: 
        # Los ataques generan un puntaje de ataque (número entero)
        # En el caso de los jugadores que tienen un arma, se debe retornar la cantidad de puntos de
        # ATK más un número al azar entre 1 y 5, en caso contrario solo se retorna los puntos de ATK
        return (self.atk + random.randint(1, 5)) if self.arma else self.atk
    
    def defensa(self, ataque: int) -> None:
        # La acción de defensa recibe un ataque (número entero) y disminuye el HP.
        # En el caso de los jugadores, al ataque recibido se le debe restar un número al azar entre 1
        # y los puntos de DF, y el resultado de ello (forzar a ser un número entero mayor a 0) se debe 
        # restar al HP
        self.hp -= max(ataque - random.randint(1, self.df), 0)
