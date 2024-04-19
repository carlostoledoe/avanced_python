#Python no existe la sobrecarga: tener dos métodos del mismo nombre

class Saludador:    
    # yo puedo recibir un numero indefinido de parámetro
    def saludar(self, *args, **kwargs): # * Desempaqueta una lista, ** Desempaqueta un diccionario
        for nombre in args:
            print('hola ' + nombre)
        for idioma, saludo in kwargs.items(): # Un diccionario de argumentos nombrados
            print(f'En {idioma} se saluda con {saludo}')

s = Saludador()
s.saludar('Cristian', sueco='hej', frances='Boujour', aleman='Hallo') #argumentos posicionales y argumentos nombrados
s.saludar('Dani', 'Mario', 'Pedro')