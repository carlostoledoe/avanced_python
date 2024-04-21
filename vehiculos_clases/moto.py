from vehiculos import Vehiculo

class Moto(Vehiculo):
    # como extra, las motos pueden tener carrito
    # Si tiene carrito, castigamos 30%
    def __init__(self, modelo, motor, rendimiento, 
        automatico=False, carrito=False): #piso al constructor
        # llamamos al contructor de la clase madre
        super().__init__(modelo, motor, rendimiento, automatico)
        #Inicilizo los atributos que son excluisvos de una moto
        self.carrito = carrito

    def get_consumo(self, kms): #piso la funcion
        consumo_normal = super().get_consumo(kms)
        if self.carrito:
            return consumo_normal * 1.3
        else:
            return consumo_normal


if __name__ == '__main__':
    gastadora = Moto('BMW GS310', 300, 30, carrito=True)
    print(gastadora.get_consumo(60))
    print(gastadora.calcular_gasto(60, 1000)) #hereda calcular gasto
    print(isinstance(gastadora, Moto)) #True
    print(isinstance(gastadora, Vehiculo)) #True