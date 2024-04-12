from a03_pelota import Termometro

class Botiquin:
    def __init__(self):
        self.insumos = []
    
    def add_termometro(self, temp_inicial):
        t = Termometro(30)
        t.celsius = -300
        self.insumos.append(t)
    
    def add_medicina(self):
        pass
    def add_gasa(self):
        pass

b = Botiquin()
b.add_termometro(20)
print(b)