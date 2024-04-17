from vehiculos import Vehiculo 

class Electrodomestico:
    def __init__(self, mAh, bateria):
        self.mAh = mAh 
        self.bateria = bateria


class Hibrido(Vehiculo, Electrodomestico):
    def __init__(self, modelo, motor, redimiento, automatico=False, mAh=0, bateria='5000 Watt'):
        #super().__init__(modelo, motor, redimiento, automatico)
        Vehiculo.__init__(self, modelo, motor, redimiento, automatico)
        Electrodomestico.__init__(self, mAh, bateria)
        self.mAh = min(mAh, 5000)


    def get_consumo(self, kms):
        consumo_normal = super().get_consumo(kms)
        return consumo_normal * (1 - self.mAh / 10000)
