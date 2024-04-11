class Pelota:
    def __init__(self, color: str, tamaño: int = 5):
        self.color = color
        self.tamaño = tamaño

    @property # Decorador. 
    def color_tamaño(self):
        return f'La pelota {self.color} es de tamaño {self.tamaño}'

p1 = Pelota('Naranja')
print(p1.tamaño)
print(p1.color_tamaño) # Pasa a ser una priedad, no se usa paréntesis



# Ahora veremos para qué se usa property

class Termometro:
    def __init__(self, celsius):
        self.__celsius = celsius

    # getter para obtenerlo
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