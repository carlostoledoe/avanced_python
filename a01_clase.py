# - Clase: Código que define qué contiene y qué hace un objeto de un tipo de dato, el cual
#          corresponde al nombre de la clase. Es como un plano o modelo para fabricar objetos.

# - Atributos: Contenedor de un valor o de un conjunto de valores, definido dentro de una 
#          clase que adquiere un tipo de dato según el valor que se le asigne. 

# - Método:  Corresponden a un bloque de código que permite realizar una tarea específica, los que
#          pueden tener o no un retorno y pueden ser con o sin parámetros. Acciones que puede realizar el objeto.





# class Persona:
#     estado = 'Humano' # Atributo de clase, se puede leer sin una instancia
#     def __init__(self, nombre, edad) -> None:
#         self.nombre = nombre # Atributo de instancia, hay que instanciar para accederlos
#         self.edad = edad
#         self.pais = 'Chile' # Atributo estático
#     def caminar(self):
#         print('Caminando...')

# print(Persona.estado) # Consultado sin instanciar el atributo de clase

# juan = Persona('Juan Carlos', 33) # Instancia u obejto de la clase Persona
# print(juan.nombre) # Consulta Atributos de Instancia
# print(juan.edad)
# print(juan.estado) 
# juan.caminar() # Ejecutando un método de instancia





#Los atributos definen la estructura. Se inicializan en el costructor
#Los métodos definene comportamiento, la logica. Usar verbos e infinitivo
#Para acceder con varible.metodo 






# class Vehiculo: # def __init__() --> Constructor
#     #Atributo de clase
#     num_vehiculo = 0 # No pertenece al objeto, pertenece a la clase, parte de
#     # Constructor
#     def __init__(self, modelo, motor, rendimiento, automatico = False): #self representa el vehículo que estamos creando
#     #  modelo, motor, rendimiento, automatico ---> atributos de la instancia
#         self.modelo = modelo
#         self.motor = motor
#         self.rendimiento = rendimiento
#         self.automatico = automatico
#         Vehiculo.num_vehiculo += 1 #NO esta amarrado a ningún vehículos

#     def get_consumo(self, kms):
#         '''Dada una catidad de kms, calcula cuantos litros de combustible necesito'''
#         consumo = kms / self.rendimiento #las intancias tienen rendimiento
#         return consumo

#     def tocar_bocina(self):
#         print('Beeeep!!!')

#     def calcular_gasto(self, kms, precio_lt_combustible):
#         litros_consumidos = self.get_consumo(kms)
#         return litros_consumidos * precio_lt_combustible


# yamaha = Vehiculo('Yamaha Enticer', 125, 35) #yamaha es un objeto. Las clases crean objeto. Es una instancia del tipo Vehiculo
# suzuki = Vehiculo('Suzuki Dzire', 1200, 20)
# corsa = Vehiculo('Chevrolette Corsa', 1300, 16, True)

# #print(type(corsa)) # <class '__main__.Vehiculo'>

# #Imprimir un atributo de instancia
# print('El atributo "modelo" del tercer objeto es ' + corsa.modelo) #accediendo a los atributos

# #Imprimir un atribucto de clase
# print(f'En total existen {Vehiculo.num_vehiculo} vehiculos')

# dist_vina_ptomontt = 1000 + 120
# print(suzuki.get_consumo(dist_vina_ptomontt))

# suzuki.tocar_bocina()

# print(f'De Viña a Pto Montt en un {suzuki.modelo} vamos a gastar: ')
# print(suzuki.calcular_gasto(1120, 1400))






#Consular a las clases:
class Video:
    formato = 'Video'
    SUB_TIPOS = ('instream', 'outstream')
class Social:
    formato = 'Social'
    SUB_TIPOS = ('facebook', 'linkedin')
class Display:
    formato = 'Display'
    SUB_TIPOS = ('tradicional', 'native')


def mostrar_formatos():
    clases_existentes = [Video, Social, Display]
    for clase in clases_existentes:
        print(f'''
{clase.formato.upper()} {clases_existentes.index(clase) + 1}
==========''')
        for tipo in clase.SUB_TIPOS:
            print(f'- {tipo}')

mostrar_formatos()