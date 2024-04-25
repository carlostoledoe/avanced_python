#Python no existe la sobrecarga: tener dos métodos del mismo nombre

# class Saludador:    
#     # yo puedo recibir un numero indefinido de parámetro
#     def saludar(self, *args, **kwargs): # * Desempaqueta una lista, ** Desempaqueta un diccionario
#         for nombre in args:
#             print('hola ' + nombre)
#         for idioma, saludo in kwargs.items(): # Un diccionario de argumentos nombrados
#             print(f'En {idioma} se saluda con {saludo}')

# s = Saludador()
# s.saludar('Cristian', sueco='hej', frances='Boujour', aleman='Hallo') #argumentos posicionales y argumentos nombrados
# s.saludar('Dani', 'Mario', 'Pedro')




# Al hacer la creación de la instancia, se debe especificar cada argumento con el nombre del parámetro al que
# corresponde, de forma tal que puedan ser almacenados en el parámetro **kwargs.

# El orden de salida de los print ha cambiado, ya que la clase PelotaDeDeporte hace un llamado al 
# constructor de la siguiente clase heredada (PelotaDePlastico) antes de ejecutar su propio print.


# Uso de super(), pero se debe tener algunas consideraciones:

# "Teniendo como ejemplo una clase hija C que hereda, de izquierda a derecha, las clases A y B,
# y que se desee ejecutar los constructores padres en el orden A, B al momento de crear una
# instancia de C"

class PelotaDeDeporte:
    def __init__(self, tamaño: int, **kwargs ) -> None:
        super().__init__(**kwargs)
        print('Creando pelota de deporte')
        self.tamaño = tamaño

class PelotaDePlastico:
    def __init__(self, material: str, **kwargs) -> None:
        super().__init__(**kwargs)
        print('Creando pelota de plástico')
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        super().__init__(**kwargs)
        print('Creando una pelota de Ping Ping')
        self.timbre = timbre

pdpp = PelotaDePingPong(tamaño=4, material='Celuloide', timbre='POWERPONG')
# Creando pelota de plástico
# Creando pelota de deporte
# Creando pelota de ping pong



