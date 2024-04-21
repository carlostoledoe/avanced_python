# Ocupar un ciclo infinito (con "0" para salir) para crear Vehiculos)
from vehiculos import Vehiculo

# lista de instancias 
mis_vehiculos = []

# 1.Ciclo infinito para ir llenado una lista
while True:
    print('\nIngrese datos del vehículo:')
    modelo = input('Ingrese modelo: ')
    if modelo == '0':
        break
    motor = int(input('Ingrese motor: '))
    rendimiento = int(input('Ingrese rendimiento: '))
    automatico = input('¿Es automático? (si/no): ')
    # if automatico == 'si':
    #     automatico = True
    # else:
    #     automatico = False
    automatico = True if automatico == 'si' else False
    
    auto_nuevo = Vehiculo(modelo, motor, rendimiento, automatico)
    mis_vehiculos.append(auto_nuevo)

# 2. Una vez terminado el ciclo, imprimir todos los modelos.
for vehiculo in mis_vehiculos:
    print(f'\nEl modelo es: {vehiculo.modelo}')
    print(f'El motor es: {vehiculo.motor}')
    print(f'El rendimiento es: {vehiculo.rendimiento}')
    print(f'Es antomático: {"Si" if vehiculo.automatico else "No"}')
