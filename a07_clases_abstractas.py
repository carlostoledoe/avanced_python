# Las clases abstractas en Python son una característica de la programación orientada a objetos
# que sirve para crear una especie de plantilla para otras clases. Se utilizan para definir
# métodos que deben ser creados por las clases que hereden de la clase abstracta, pero sin
# implementar la funcionalidad completa. Esto es útil para asegurar que ciertos métodos sean
# implementados en todas las subclases, manteniendo una estructura coherente y evitando la duplicación de código.
# No se puede instanciar con una clase abstracta

from abc import ABC, abstractmethod

# Definición de la clase abstracta
class FiguraGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Implementación de una subclase concreta
class Circulo(FiguraGeometrica):
    
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

# Uso de la subclase
circulo = Circulo(5)
print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")
