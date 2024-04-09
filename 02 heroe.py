class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.hp = health
        self.bag = []

    def gritar(self):
        print(f'BAZAAAAYYY!!! yo, {self.name}, te voy a matate a ti')

aragon = Hero('Aragon', 100, 10)
aragon.gritar()