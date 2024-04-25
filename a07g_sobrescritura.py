# class PelotaDeDeporte:
#     def __init__(self, color: str) -> None:
#         self.__color = color

#     @property
#     def color(self):
#         return self.__color

#     @color.setter
#     def _color(self, value):
#         self.__color = value

# class PelotaDeTenis(PelotaDeDeporte):
#     def __init__(self) -> None: # sobrescrita del constructor
#         self.__color = 'Amarillo' 

#     @property
#     def color(self):
#         return self.__color

#     @color.setter
#     def color(self, value):
#         pass

# pdt = PelotaDeTenis()
# pdt.color = 'Rojo'
# print(pdt.color)








# super()
# Para hacer el llamado al método de la clase padre, se puede hacer mediante super(), sin argumentos .

# class PelotaDeDeporte:
#     def __init__(self, color: str) -> None:
#         self._color = color

#     @property
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, value):
#         self._color = value

# class PelotaDeFutbol(PelotaDeDeporte):
#     def __init__(self, color: str, cantidad_hexagonos: int) -> None:
#         super().__init__(color) # se ejecuta constructor de PelotaDeDeporte
#         self._cantidad_hexaganos = cantidad_hexagonos

#     @property
#     def cantidad_hexaganos(self):
#         return self._cantidad_hexaganos

# pdf = PelotaDeFutbol('Blanco y Negro', 15)
# print(pdf.color) # Blanco y Negro
# print(pdf.cantidad_hexaganos) # 15





# Herencia multiple
# "El problema del diamante"

# Si un método es heredado (desde una clase A) y sobrescrito por dos clases (B y C), las
# cuales luego en conjunto son heredadas por una cuarta clase (D), no queda claro cuál de
# los métodos será ejecutado al ser llamado desde la última clase de la jerarquía (D).
# Esto Python lo resuelve según el orden en el cual se heredan las clases, de forma tal que se
# preservará en la clase hija lo definido en la primera clase heredada (declarada de izquierda
# a derecha) que lo posee. Esta misma regla se aplica a todas las clases superiores de la
# jerarquía, siendo esto gestionado por el MRO (“Method Resolution Order”) de Python.



# Sobreescritura de constructor en herencia múltiple
# Una forma de lograr que se ejecute el constructor de más de una clase heredada al
# momento de crear una instancia de la clase hija, es haciendo el llamado al constructor
# directamente desde las clases padres. 

# Cada llamado debe recibir como argumentos self y luego todos los argumentos
# requeridos en cada caso. Esta forma de hacer uso del constructor en una clase heredada
# también es posible en herencia simple. 


# class PelotaDeDeporte():
#     def __init__(self, tamaño: int):
#         print("Creando pelota de deporte")
#         self.tamaño = tamaño

# class PelotaDePlastico():
#     def __init__(self, material: str):
#         print("Creando pelota de plástico")
#         self.material = material

# class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
#     def __init__(self, tamaño: int, material: str, timbre: str):
#         PelotaDeDeporte.__init__(self, tamaño)
#         PelotaDePlastico.__init__(self, material)
#         print("Creando pelota de ping pong")
#         self.timbre = timbre

# pdpp = PelotaDePingPong(4, "celuloide", "POWERTI")
# # Creando pelota de deporte
# # Creando pelota de plástico
# # Creando pelota de ping pong



# Otra forma
# Se puede realizar mediante el uso de super(), pero se debe tener algunas
# consideraciones: 
# "Teniendo como ejemplo una clase hija C que hereda, de izquierda a derecha, las clases A y B,
# y que se desee ejecutar los constructores padres en el orden A, B al momento de crear una
# instancia de C"





