from apodekex import APokedex
class Pokedex(APokedex):
    def __init__(self) -> None:
        self.my_pokemons = []
    def listPokemon(self):
        for pokemon in self.my_pokemons:
            print(self.pokemonInfo(pokemon))
    def createPokemon(self, name, health, tipo): #pisar método
        nuevo_pokemon = super().createPokemon(name,health, tipo)
        self.my_pokemons.append(nuevo_pokemon)

if __name__ == '__main__':
    dex = Pokedex()
    p1 = dex.createPokemon('Pikachu', 50, 'Electrico')
    # dex.my_pokemons.append(p1)
    p2 = dex.createPokemon('Snorlax', 60, 'Normal')
    # dex.my_pokemons.append(p2)
    dex.listPokemon()
    print('>>> Después del ataque <<<')
    dex.my_pokemons[0].attack(dex.my_pokemons[1])
    dex.listPokemon()