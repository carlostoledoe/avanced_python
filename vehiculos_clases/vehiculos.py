class Vehiculo:
    num_vehiculo = 0 
    def __init__(self, modelo, motor, rendimiento, automatico = False): 
        self.modelo = modelo
        self.motor = motor
        self.rendimiento = rendimiento
        self.automatico = automatico
        Vehiculo.num_vehiculo += 1

    def get_consumo(self, kms):
        consumo = kms / self.rendimiento 
        return consumo

    def tocar_bocina(self):
        print('Beeeep!!!')

    def calcular_gasto(self, kms, precio_lt_combustible):
        litros_consumidos = self.get_consumo(kms)
        return litros_consumidos * precio_lt_combustible



if __name__ == '__main__':
    yamaha = Vehiculo('Yamaha Enticer', 125, 35) 
    suzuki = Vehiculo('Suzuki Dzire', 1200, 20)
    corsa = Vehiculo('Chevrolette Corsa', 1300, 16, True)

    print('El atributo "modelo" del tercer objeto es ' + corsa.modelo) 
    print(f'En total existen {Vehiculo.num_vehiculo} vehiculos')

    dist_vina_ptomontt = 1000 + 120
    print(suzuki.get_consumo(dist_vina_ptomontt))

    suzuki.tocar_bocina()

    print(f'De Viña a Pto Montt en un {suzuki.modelo} vamos a gastar: ')
    print(suzuki.calcular_gasto(1120, 1400))
