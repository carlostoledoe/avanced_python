from personaje import Personaje

class Monstruo(Personaje):
    def ataque(self) -> int:
    # En el caso de los monstruos, debe retornar los puntos de ATK más el 1% del HP actual
    # (retorna un número entero).
        return self.atk + int(self.hp * 0.01)
    
    def defensa(self, ataque: int) -> None:
        # En el caso de los monstruos, al ataque recibido se le debe restar los puntos de DF y el
        # 0.1% del HP actual, y el resultado de ello (forzar a ser un número entero mayor a 0) se
        # debe restar al HP.
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)
