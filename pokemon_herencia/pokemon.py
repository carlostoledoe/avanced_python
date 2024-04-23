class Pokemon:
    count = 0 # Cantidad de pokemones que llevamos
    def __init__(self, name, health, tipo) -> None:
        self._name = name
        self._health = health
        self._tipo = tipo
        Pokemon.count += 1 

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def tipo(self):
        return self._tipo

    def attack(self, otro_pokemon):
        otro_pokemon.health = otro_pokemon.health - 10 # Al atacar, le quita 10 al otro pokemon

if __name__ == '__main__':
    p1 = Pokemon('Pikachu', 50, 'Eléctrico')
    p2 = Pokemon('Rengar', 60, 'Sombras')
    p1.attack(p2)
    # p1.name = 'Hola' # No se pude
    print(p1.name)
    print(p2.health)
    print(Pokemon.count)