class Vehiculo:
    num_vehiculo = 0 
    def __init__(self, modelo, motor, rendimiento, automatico = False): 
        self.modelo = modelo
        self.motor = motor
        self.rendimiento = rendimiento
        self.automatico = automatico
        Vehiculo.num_vehiculo += 1 