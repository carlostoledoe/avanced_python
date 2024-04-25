from abc import ABC, abstractmethod
class Personaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self._hp = hp
        self._atk = atk
        self._df = df
    
    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, hp) -> None:
        self._hp = hp
    
    @property
    def atk(self) -> int:
        return self._atk
    
    @property
    def df(self) -> int:
        return self._df
    
    @abstractmethod
    def ataque(self) -> None:
        pass
    
    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass
