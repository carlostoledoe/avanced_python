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
        pass

if __name__ == '__main__':
    aragon = Personaje('Aragon')
    aragon.set_estado(50)
    aragon.set_estado(50)
    aragon.set_estado(-30)

    aragon.get_estado()
