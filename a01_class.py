# yahama = {
#     'modelo': 'Yamaha Enticer',
#     'motor': 125,
#     'rendimiento': 35,
#     'automatico': False
# }

# suzuki = {
#     'modelo': 'Suzuki Dezire',
#     'motor': 1200,
#     'rendimiento': 20,
#     'automatico': False
# }

# corsa = {
#     'modelo': 'Chevrolette Corsa',
#     'motor': 1300,
#     'rendimiento': 16,
#     'automatico': True
# }


class Vehiculo: # def __init__() --> Constructor
    #Atributo de clase
    num_vehiculo = 0 # No pertenece al objeto, pertenece a la clase, parte de
    #  modelo, motor, rendimiento, automatico ---> atributos de la instancia
    # Constructor
    def __init__(self, modelo, motor, rendimiento, automatico = False): #self representa el vehículo que estamos creando
        self.modelo = modelo
        self.motor = motor
        self.rendimiento = rendimiento
        self.automatico = automatico
        Vehiculo.num_vehiculo += 1 #NO esta amarrado a ningún vehículos

    def get_consumo(self, kms):
        '''Dada una catidad de kms, calcula cuantos litros de combustible necesito'''
        consumo = kms / self.rendimiento #las intancias tienen rendimiento
        return consumo

    def tocar_bocina(self):
        print('Beeeep!!!')

    def calcular_gasto(self, kms, precio_lt_combustible):
        litros_consumidos = self.get_consumo(kms)
        return litros_consumidos * precio_lt_combustible


yamaha = Vehiculo('Yamaha Enticer', 125, 35) #yamaha es un objeto. Las clases crean objeto. Es una instancia del tipo Vehiculo
suzuki = Vehiculo('Suzuki Dzire', 1200, 20)
corsa = Vehiculo('Chevrolette Corsa', 1300, 16, True)

#print(type(corsa)) # <class '__main__.Vehiculo'>

#Imprimir un atributo de instancia
print('El atributo "modelo" del tercer objeto es ' + corsa.modelo) #accediendo a los atributos

#Imprimir un atribucto de clase
print(f'En total existen {Vehiculo.num_vehiculo} vehiculos')

dist_vina_ptomontt = 1000 + 120
print(suzuki.get_consumo(dist_vina_ptomontt))

suzuki.tocar_bocina()

print(f'De Viña a Pto Montt en un {suzuki.modelo} vamos a gastar: ')
print(suzuki.calcular_gasto(1120, 1400))


#Los atributos definen la estructura. Se inicializan en el costructor
#Los métodos definene comportamiento, la logica. Usar verbos e infinitivo
#Para acceder con varible.metodo 
