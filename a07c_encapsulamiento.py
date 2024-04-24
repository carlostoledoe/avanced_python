# Encapsulamiento:
# Este principio permite agrupar los datos (atributos) y los métodos (funciones) 
# que manipulan esos datos en una unidad, la clase, y restringir el acceso a algunos componentes 
# internos de esa clase.


# Delimita un conjunto de datos, y los métodos que afectan esos datos, dentro de una misma
# unidad, restringiendo así el acceso y uso de los datos y métodos “encapsulados”. Un
# ejemplo clásico corresponde a una Clase, ya que dentro de su estructura encierra todos los
# métodos y atributos que permiten definir un objeto de dicha clase. 


# Mediante la abstracción, es posible establecer la pauta a seguir para todas las subclases
# que comparten comportamientos en común, dados por la clase base, por otro lado, el
# encapsulamiento permite delimitar dentro de una clase todo el comportamiento y estado de
# cada objeto instanciado a partir de dicha clase


# Convenciones en Python:
#   - Atributo Público: Se puede acceder desde cualquier lugar.
#   - Atributo Protegido (_): Por convención, no debería ser accesado directamente desde fuera de 
#     la clase, excepto en subclases. No es una regla estricta, sino más bien una convención entre programadores.
#   - Atributo Privado (__): Python realiza un cambio de nombre (name mangling) que dificulta su acceso 
#   - desde fuera de la clase, aunque técnicamente sigue siendo posible.




# class CuentaBancaria:
#     def __init__(self, propietario, saldo=0):
#         self.propietario = propietario
#         self._saldo = saldo

#     @property 
#     def saldo(self): #se accede como un propiedad, es un Getter ( cuenta.saldo (se obtiene el saldo))
#         """ Getter para saldo que permite acceso controlado al atributo protegido _saldo """
#         return self._saldo

#     @saldo.setter
#     def saldo(self, cantidad): # Se accede como una propiedad cuenta.saldo = 500 (nuevo saldo)
#         """ Setter para saldo que impide establecer un saldo negativo """
#         if cantidad < 0:
#             print("El saldo no puede ser negativo.")
#         else:
#             self._saldo = cantidad
#             print(f"Saldo actualizado a: {cantidad}")

#     @saldo.deleter
#     def saldo(self):
#         """ Deleter para saldo que permite borrar el saldo, estableciéndolo a cero """
#         self._saldo = 0
#         print("Saldo borrado y establecido a cero.")

#     def depositar(self, cantidad):
#         if cantidad > 0:
#             self.saldo += cantidad
#             print(f"Depósito exitoso: {cantidad}")
#         else:
#             print("El monto a depositar debe ser positivo.")

#     def retirar(self, cantidad):
#         if 0 < cantidad <= self.saldo:
#             self.saldo -= cantidad
#             print(f"Retiro exitoso: {cantidad}")
#         else:
#             print("Fondos insuficientes.")

# # Uso de la clase con decoradores
# cuenta = CuentaBancaria("Juan", 100)
# cuenta.depositar(200)
# print(cuenta.saldo)  # Usando el getter de saldo
# cuenta.saldo = 300  # Usando el setter de saldo
# print(cuenta.saldo)
# del cuenta.saldo  # Usando el deleter de saldo
# print(cuenta.saldo)









# from abc import ABC, abstractmethod

# class Pelota(ABC):
#     @abstractmethod
#     def rebotar(self, altura: int):
#         pass

# class PelotaDeJuguete(Pelota):
#     def __init__(self, color) -> None:
#         self.__color = color
    
#     @property
#     def color(self): # Como se está dentro de la clase, sí puede acceder al atributo aunque sea privado
#         return self.__color
    
#     @color.setter
#     def color(self, nuevo_color: str): # Puede modificar el atributo privado, porque está dentro de la clase
#         self.__color = nuevo_color
    
#     def rebotar(self, altura: int):
#         pass

# p = PelotaDeJuguete("amarilla")
# print(p.color)
# # print(p.__color) #Error
# print(p._PelotaDeJuguete__color) 
