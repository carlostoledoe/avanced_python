# Accesadores (getters) y Mutadores (setters)
# @property: Al utilizarlo se está “definiendo una propiedad de la clase”
# En la instancia creada, para hacer uso de un accesador basta con usar la sintaxis de punto .
#  y el nombre de la propiedad (sin paréntesis al final, tal como si fuera un atributo). 
# En el caso del mutador, este es invocado al hacer uso del signo =
# @property se utiliza para definir un método que se comporta como un atributo de solo lectura, 
# mientras que @setter se utiliza para definir un método que asigna un valor a un atributo


# class Persona:
#     def __init__(self, nombre:str, edad:int) -> None:
#         self._nombre = nombre
#         self._edad = edad
        
#     @property
#     def nombre(self): # puede ser llamado como juan.nombre 
#         return self._nombre 
#     @nombre.setter
#     def nombre(self, nuevo_nombre):
#         self._nombre = nuevo_nombre
    
#     @property
#     def edad(self):
#         return self._edad
#     @edad.setter
#     def edad(self, nueva_edad):
#         if nueva_edad >= 0:
#             self._edad = nueva_edad
#         else:
#             raise ValueError('La edad debe ser mayor a cero')

# # Uso de la clase Persona
# juan = Persona('Juan', 30)
# print(juan.nombre)
# print(juan.edad)

# # Cambio de nombre usanod metodo setter
# juan.nombre = 'Pedro'
# juan.edad = 40
# print(juan.nombre)
# print(juan.edad)









# class Temperatura:
#     def __init__(self, celsius=0) -> None:
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError('La temperatura no puede ser menor a -273.15')
#         self._celsius = value


# # Crear objeto y establecer temperatura
# t = Temperatura()
# t.celsius = 25
# print(t.celsius)
# t.celsius = -274
# print(t.celsius)








# class Persona:
#     def __init__(self, nombre) -> None:
#         self._nombre = nombre
#     @property
#     def nombre(self):
#         return self._nombre
#     @nombre.setter
#     def nombre(self, nuevo_nombre:str):
#         if not nuevo_nombre.isalpha():
#             raise ValueError('El nombre debe contener solo letras')
#         self._nombre = nuevo_nombre

# pedro = Persona('Pedro')
# pedro.nombre = 'Maria'
# print(pedro.nombre)
# pedro.nombre = 'Maria 33'
# print(pedro.nombre)







# class Pelota:
#     def __init__(self) -> None:
#         self._tamaño = 1
#     @property
#     def tamaño(self):
#         return self._tamaño
#     @tamaño.setter
#     def tamaño(self, nuevo_tamaño):
#         self._tamaño = nuevo_tamaño if nuevo_tamaño > 0 else 4

# p = Pelota()
# p.tamaño = -1
# print(p.tamaño)









# class Medicameto():
#     iva = 0.18
#     def __init__(self, nombre: str, stock: int = 0) -> None:
#         self._nombre = nombre
#         self._stock = stock
#         self._precio_bruto = 0
#         self._precio_final = 0
#         self._descuento = 0
#     @property
#     def descuento(self):
#         return self._descuento
#     @property
#     def precio_final(self):
#         return self._precio_final
#     @staticmethod
#     def validar_numero(numero: int):
#         return numero > 0
#     @property
#     def precio(self):
#         return self._precio_final
#     @precio.setter
#     def precio(self, precio_bruto: int):
#         if self.validar_numero(precio_bruto):
#             self._precio_bruto = precio_bruto
#             self._precio_final = precio_bruto + precio_bruto * self.iva
#             if self._precio_final >= 10000 and self._precio_final < 20000:
#                 self._descuento = 0.1
#             elif self._precio_final >= 20000:
#                 self._descuento = 0.2
#             if self._descuento:
#                 self._precio_final *= 1 - self._descuento

# nombre = input("Ingrese nombre del medicamento: ")
# stock = int(input("Ingrese stock del medicamento: "))
# precio_bruto = int(input("Ingrese precio bruto del medicamento: "))

# m1 = Medicameto(nombre, stock)
# m1.precio = precio_bruto

# if m1.descuento: #si hay descuento
#     print(f"Tiene un descuento de {m1.descuento * 100}%")

# print(f'El precio final del medicamento es {m1.precio_final}')
