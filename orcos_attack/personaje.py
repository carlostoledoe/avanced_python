import random
import time

class Personaje:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._nivel = 1
        self._experiencia = 0

    @property
    def nombre(self):
        return self._nombre

    @property   
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, value):
        self._experiencia = value

    def get_estado(self):
        print(f'NOMBRE: {self.nombre}      NIVEL: {self.nivel}      EXP: {self.experiencia}')
    
    def set_estado(self, exp_recibida: int):
        nueva_experiencia = self.experiencia + exp_recibida
        if nueva_experiencia < 0:
            nueva_experiencia = 0 
        niveles_cambiados = nueva_experiencia // 100
        nueva_experiencia = nueva_experiencia % 100

        self.nivel += niveles_cambiados
        self.nivel = max(1, self.nivel)
        self.experiencia = nueva_experiencia

    
    def __gt__(self, otro: object) -> bool:
        return True if self.nivel > otro.nivel else False
    
    def __lt__(self, otro: object) -> bool:
        return True if self.nivel < otro.nivel else False
    
    def __eq__(self, otro: object) -> bool:
        return True if self.nivel == otro.nivel else False
    
    def probabilidad_ganar(self, otro: object) -> float:
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        elif self == otro:
            return 0.50 

    @staticmethod
    def orco_visible(probabilidad):
        return f'\nCon tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.'

    def attack(self, probabilidad, otro: object):
        numero_aleatorio = random.uniform(0, 1)
        resultado = 'gana' if numero_aleatorio < probabilidad else 'pierde'
        if resultado == 'gana':
            print('\n>>> ¡Le has ganado al Orco! <<<')
            time.sleep(1)
            print('\n¡Recibirás 50 puntos de experiencia!\n')
            self.set_estado(50)
            otro.set_estado(-30)
        elif resultado == 'pierde':
            print('\n>>> ¡Oh no! ¡El orco te ha ganado! <<<')
            time.sleep(1)
            print('\n¡Has perdido 30 puntos de experiencia!\n')
            self.set_estado(-30)
            otro.set_estado(50)


if __name__ == '__main__':
    aragon = Personaje('Aragon')
    orco = Personaje('Orco')
    aragon.set_estado(350)
    aragon.set_estado(-150)
    orco.set_estado(100)
    orco.set_estado(30)
    orco.set_estado(-15)

    aragon.get_estado()
    orco.get_estado()

    print('Comparación:')
    orco = Personaje('Orco')
    print(aragon > orco) 
    print(aragon < orco)
    print(aragon == orco)