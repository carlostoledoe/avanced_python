# Las clases abastractas definen un compromiso. Cuando tienen muchas clases y quiero que todas 
# hagan algo. El objetivo es ailsar el compotamiento
from abc import ABC, abstractmethod # abstract base class

class ACredito(ABC): # Comenzar con A es una convención. Esta clase es hija de ABC
    @abstractmethod
    def definir_monto(self, valor):
        pass
    def mostrar_monto(self):
        return self.valor


class CredConsumo(ACredito): #CredConsumo tiene que cumplir el compromiso de definirlo en la clase hijo. Hereda la clase Acredito.
    ''' EL monto debe ir entre 1MM y 5MM'''
    def __init__(self): 
        self.monto = None
        self.email = None

    # Modificar el monto
    def definir_monto(self, valor):
        if valor < 1_000_000:
            self.valor = 1_000_000
        elif valor > 5_000_000:
            self.valor = 5_000_000
        else:
            self.valor = valor

    def __str__(self) -> str:
        return f'Credito de Consumo de ${self.valor}'

    # Agregar un email


class CredHipotecario(ACredito):
    '''EL monto debe ir entre 20MM y 100MM'''
    def __init__(self):
        self.monto = None
        self.email = None

    # Modificar el monto
    def definir_monto(self, valor):
        if valor > 100_000_000:
            self.valor = 100_000_000
        elif valor < 20_000_000:
            self.valor = 20_000_000
        else:
            self.valor = valor

    def __str__(self) -> str:
        return f'Credito de Hipotecario de ${self.valor}'

    # Agregar un email

