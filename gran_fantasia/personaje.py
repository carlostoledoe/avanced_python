import random

class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0
    
    def __gt__(self, otro_personaje): #sobreescritura great than  >
        if self.nivel > otro_personaje.nivel:
            return True
        else:
            return False
    
    def __lt__(self, otro_personaje): #sobreescritura less than  <
        if self.nivel < otro_personaje.nivel:
            return True
        else:
            return False
    
    def estado(self):
        return print(f'NOMBRE: {self.nombre}      NIVEL: {self.nivel}     EXP: {self.exp}')
    
    def mod_estado(self, exp):
        nueva_exp = self.exp + exp
        diff_niveles = nueva_exp // 100
        self.exp = nueva_exp % 100
        self.nivel += diff_niveles



if __name__ == '__main__':
    aragon = Personaje('Aragon')
    aragon.mod_estado(50)
    aragon.mod_estado(50)
    aragon.mod_estado(-30)
    aragon.estado()





# Si gana heroe :  + 50 puntos experiencia y el orco pierde - 30 pts
# Si pierdde heroe : - 30 pts y el ocorco gana + 50 pts
