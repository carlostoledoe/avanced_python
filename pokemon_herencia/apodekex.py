from ipokedex import Ipokedex
from pokemon import Pokemon

class APokedex(Ipokedex):
    def createPokemon(self, name, health, tipo):
        pokemon = Pokemon(name, health, tipo)
        return pokemon
    def pokemonInfo(self, pokemon):
        return f'El pokemon {pokemon.name} de tipo {pokemon.tipo} tiene {pokemon.health} punto de vida'

if __name__ == '__main__':
    dex = APokedex()
    p1 = dex.createPokemon('Pikachuuu', 100, 'Electrico')
    p2 = dex.createPokemon('Snorlax', 300, 'Normal')
