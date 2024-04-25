from abc import ABC, abstractmethod
from sin_gluten import SinGluten

class Chocolate(ABC):
    def __init__(self, porcentaje_cacao) -> None:
        self.porcentaje_cacao = self.validar_cacao(porcentaje_cacao)
    
    @abstractmethod
    def validar_cacao(self, porcentaje: float) -> float:
        pass

class ChocolateAmargo(Chocolate):
    def validar_cacao(self, porcentaje: float) -> float:
        return min(max(0.75, porcentaje), 0.85) # si el valor entregado es menor a 0.75, 
    # se retorna 0.75; si el valor entregado es mayor a 0.85, se retorna 0.85. 
    # En cualquier otro caso, se retorna el valor entregado.

class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass


if __name__ == '__main__':
    choco = ChocolateAmargo(0.3)
    print(choco.porcentaje_cacao) # 0.75