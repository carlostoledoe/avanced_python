class Hero:
    num_heroes = 0 # estático, pertenece a la clase
    def __init__(self, name: str, health: int, power: int = 10): # Constructor, sino lo declaro, queda vacío, problema de scoping
        self.name = name
        self.health = health
        self.power = power
        self.hp = health
        self.bag = []
        Hero.num_heroes += 1
    @staticmethod #son como métodos generales. Son como una función, no requieren instancia
    def print_num_heroes():
        print(f'En este momento hay {Hero.num_heroes} heroes')
    
    def gritar(self):
        print(f'BAZAAAAYYY!!! yo, {self.name}, te voy a matate a ti')
    
    def atack(self, victim):
        victim.hp -= self.power
    
    @staticmethod
    def is_dead(person_hp):
        if person_hp <= 0:
            return True
        else:
            return False

aragon = Hero('Aragon', 100, 10) #primera instancia
rayhar = Hero('Rayhar', 100, 12)
yamcha = Hero('Yamcha', 10, 2)

gohan = Hero(300, True, 'Hola') #Esto no se puede restrigir hasta el momento.

aragon.gritar() #aragon es una instancia de la clase Hero
Hero.print_num_heroes()
aragon.atack(rayhar)
print(f'{rayhar.name} tiene {rayhar.hp} de vida')
print(Hero.is_dead(aragon.hp)) #false, ya que tiene HP positivo
rayhar.atack(yamcha)
print(f'{yamcha.name} está Muerto' if Hero.is_dead(yamcha.hp) else f'{yamcha.name} está Vivo')
print(type(gohan.name))