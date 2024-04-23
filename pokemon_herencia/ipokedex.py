from abc import ABC, abstractmethod

class Ipokedex(ABC): #Clase asbtracta que no implementa nada
    
    @abstractmethod # Delego a las hijas que lo ejecuten
    def createPokemon(self, name, health, tipo):
        pass
    
    @abstractmethod
    def pokemonInfo(self, pokemon):
        pass
    
    @abstractmethod
    def listPokemon(self):
        pass


if __name__ == '__main__':
    drex = Ipokedex()
