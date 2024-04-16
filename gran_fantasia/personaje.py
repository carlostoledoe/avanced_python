import random

prob_soy_mejor = ['gana', 'gana', 'pierde']
prob_soy_peor = ['gana', 'pierde', 'pierde']
prob_soy_igual = ['gana', 'pierde']

class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.__nivel = 1
        self.__exp = 0
    
    def __gt__(self, otro_personaje): #sobreescritura great than  >
        if self.__nivel > otro_personaje.nivel:
            return True
        else:
            return False
    
    def __lt__(self, otro_personaje): #sobreescritura less than  <
        if self.__nivel < otro_personaje.nivel:
            return True
        else:
            return False
    
    def get_estado(self):
        return print(f'NOMBRE: {self.nombre}      NIVEL: {self.__nivel}     EXP: {self.__exp}')
    
    def set_estado(self, ptos_exp):
        nueva_exp = self.__exp + ptos_exp
        if nueva_exp < 0:
            niveles_por_bajar = 1 + (nueva_exp // 100)
            self.__nivel = max(1, self.__nivel - niveles_por_bajar)
            self.__exp = max(0, 100 + nueva_exp)
        else:
            self.__exp = nueva_exp % 100
            self.__nivel = nueva_exp // 100

    # @estado.setter
    # def estado(self, exp):
    #     tmp_exp = self.experiencia + exp
    #     while tmp_exp >= 100:
    #         self.nivel += 1
    #         tmp_exp -= 100
    #     while tmp_exp < 0:
    #         if self.nivel > 1:
    #             tmp_exp = 100 + tmp_exp
    #             self.nivel -= 1


    def atacar(self, otro):
        if self > otro:
            random.choice(prob_soy_mejor)
        elif self < otro:
            random.choice(prob_soy_peor)
        else: # niveles iguales
            random.choice(prob_soy_igual)



if __name__ == '__main__':
    aragon = Personaje('Aragon')
    aragon.set_estado(50)
    aragon.set_estado(50)
    aragon.set_estado(-30)
    aragon.get_estado()





# Si gana heroe :  + 50 puntos experiencia y el orco pierde - 30 pts
# Si pierdde heroe : - 30 pts y el ocorco gana + 50 pts
