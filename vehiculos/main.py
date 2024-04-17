from vehiculos import Vehiculo
from hibrido import Hibrido
from moto import Moto

if __name__ == '__main__':
    susuki = Vehiculo('Dzire', 1200, 20)
    moto = Moto('BMW GS310', 300, 30, carrito=True)
    hi = Hibrido('Kia Niro Hev', 1600, 20, mAh=3000 )

    distancia = 1120

    vehiculos = [susuki, moto, hi]
    for v in vehiculos:
        print(v.get_consumo(distancia))
