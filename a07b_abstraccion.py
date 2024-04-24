# Abastracción:
# La abstracción es un principio fundamental que se refiere a ocultar los detalles complejos 
# de implementación y exponer solo las características y comportamientos esenciales de un objeto. 
# Esto permite a los desarrolladores trabajar con conceptos más simples, interactuando con los 
# objetos de manera más intuitiva y sin preocuparse por los detalles internos.


# Mediante la abstracción, es posible establecer la pauta a seguir para todas las subclases
# que comparten comportamientos en común, dados por la clase base, por otro lado, el
# encapsulamiento permite delimitar dentro de una clase todo el comportamiento y estado de
# cada objeto instanciado a partir de dicha clase



# En Python, para trabajar con clases y métodos abstractos, utilizamos el módulo `abc` (Abstract Base Classes).
# Una clase abstracta es una clase que no puede ser instanciada directamente y que está destinada 
# ser la clase base para otras subclases. Un método abstracto dentro de una clase abstracta es un método que
# se declara, pero no se implementa en la clase abstracta; en cambio, debe ser implementado por las subclases 
# que hereden de esta clase abstracta.


# Para definir una clase abstracta y métodos abstractos, seguirás los siguientes pasos:

# 1. Importa `ABC` y `abstractmethod` desde el módulo `abc`.
# 2. Declara una clase que herede de `ABC`.
# 3. Decora los métodos que deseas que sean abstractos con el decorador `@abstractmethod`.

# Vamos a ver un ejemplo de una clase abstracta que define una estructura para vehículos, 
# pero deja la implementación de algunos métodos a las clases que la hereden:






# from abc import ABC, abstractmethod

# class Vehiculo(ABC):
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     @abstractmethod
#     def arrancar(self):
#         """ Método para arrancar el vehículo, debe ser implementado por cada subclase """
#         pass

#     @abstractmethod
#     def detener(self):
#         """ Método para detener el vehículo, debe ser implementado por cada subclase """
#         pass

#     def mostrar_informacion(self):
#         """ Método concreto que es el mismo para todas las subclases """
#         print(f"Vehículo {self.marca} modelo {self.modelo}")

# # Clase concreta que hereda de Vehiculo
# class Coche(Vehiculo):
#     def arrancar(self):
#         print(f"El coche {self.marca} {self.modelo} ha arrancado.")

#     def detener(self):
#         print(f"El coche {self.marca} {self.modelo} se ha detenido.")

# # Intentando crear una instancia de la clase abstracta (esto lanzará un error)
# # mi_vehiculo = Vehiculo("Generic", "1234")  # Esto no es posible

# # Creando una instancia de la subclase
# mi_coche = Coche("Toyota", "Corolla")
# mi_coche.arrancar()
# mi_coche.detener()
# mi_coche.mostrar_informacion()






# Puntos clave:
# Clase abstracta 'Vehiculo' : No puede ser instanciada directamente. Tiene métodos 
# abstractos 'arrancar()' y 'detener()' que no tienen implementación.

# Clase concreta 'Coche': Hereda de 'Vehiculo' y debe implementar los métodos 'arrancar()' y 'detener()'. 
# También puede utilizar o sobrescribir métodos concretos como 'mostrar_informacion()'.

# Al intentar instanciar directamente una clase abstracta, Python lanzará un `TypeError` indicando que 
# las clases con métodos abstractos no pueden ser instanciadas. Esto asegura que solo se puedan crear 
# instancias de subclases que implementen todos los métodos abstractos requeridos, manteniendo la
# coherencia y cumpliendo con el diseño orientado a objetos.











# from abc import ABC, abstractmethod

# class Pelota(ABC): # Clase abstracta, no se puede instanciar
#     @abstractmethod
#     def rebotar(self, altura: int): #Método abstracto, no tiene implementación
#         pass
# #pelota = Pelota() # TypeError: Can't instantiate abstract class Pelota with abstract method rebotar

# class PelotaDeJuguete(Pelota):
#     def __init__(self) -> None:
#         self.rebotes = []
    
#     def rebotar(self, altura: int):
#         self.rebotes = []
#         while altura > 0:
#             self.rebotes.append(altura)
#             self.rebotes.append(0)
#             altura //= 2
#         return self.rebotes

# pelota = PelotaDeJuguete()
# pelota.rebotar(100)
# print(pelota.rebotes)













