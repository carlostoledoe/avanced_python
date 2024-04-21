class Termometro:
    def __init__(self, celsius):
        self.__celsius = celsius #Atributo privado

    # getter para obtener el atributo privado
    @property
    def celsius(self):
        if self.__celsius > 100:
            return 'Novaya xq se va a morir'
        return self.__celsius
    
    #setter para controlar para controlar la propiedad interna
    @celsius.setter
    def celsius(self, temp):
        if temp < -273:
            print('No se puede bajar de los -273°C')
            return
        self.__celsius = temp
    
    def farenheit(self):
        return (self.__celsius * 1.8) + 32 # __celsius para no acceder. Es una restricción. Atributo privado

t1 = Termometro(30)
print(t1.celsius) # Por eso no se puede acceder
#t1.celsius = -300 # para evitar esto
t1.celsius = 300 # para evitar esto
print(t1.celsius)