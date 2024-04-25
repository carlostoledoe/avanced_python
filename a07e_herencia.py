# Herencia

# Mecanismo que permite derivar una clase, para crear una jerarquía de clases que
# comparten los mismos atributos y métodos.

#   - La clase padre define un conjunto de atributos y métodos que describen un
#     comportamiento común del conjunto de clases hijas que le heredan.
#   - Las clases hijas heredan tanto los atributos como el comportamiento de la clase
#     padre, pudiendo, además, añadir otros atributos y otros comportamientos.
#  - Los comportamientos (métodos) heredados pueden ser reescritos para modificar la
#    lógica según se requiera en la clase hija, esto último se verá más adelante.



# class PelotaDeDeporte:
#     def __init__(self, color: str) -> None:
#         self._color = color
#     @property
#     def color(self) -> str:
#         return self._color

# class PelotaDeFutbol(PelotaDeDeporte):
#     def mostrar_color(self):
#         print(f'Mi color es {self.color}')

# pdf = PelotaDeFutbol('Blanco y Negro')

# pdf.mostrar_color()







# Herencia múltiple
# Consiste en que una clase hija hereda más de una clase padre, es decir, la clase hija poseerá
# todos los atributos y métodos de todas las clases heredadas. 
# Si un atributo o método se encuentra en más de una de las clases heredadas, se considerará 
# los definidos en la primera clase heredada de derecha a izquierda. 

# class PelotaDeDeporte:
#     tipo = "Deporte"

# class PelotaDePlastico:
#     tipo = "Plástico"

# class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
#     pass

# print(PelotaDePingPong.tipo) # Salida: "Deporte"








