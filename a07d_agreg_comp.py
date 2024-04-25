# Colaboración
# Que una clase colabore con otra,quiere decir que una clase debe ser instanciada dentro de la otra
# Los objetos que forman parte de una colaboración no dependen uno del otro para existir.

# class Superficie:
#     def __init__(self) -> None:
#         self.__resistencia = 2

#     @property
#     def resistencia(self):
#         return self.__resistencia

# class Pelota:
#     def rebotar(self, altura: float):
#         s = Superficie()  # Se instancia la clase que colabora con Pelota
#         rebotes = []
#         while altura > 0:
#             rebotes.append(altura)
#             rebotes.append(0)
#             altura //= s.resistencia # La instancia Superficie colabora con Pelora para rebotar
#         return rebotes

# p = Pelota()
# print(p.rebotar(10))


# Composición:
# La composición es otra forma de interacción entre objetos de distinta clase, donde una
# clase tiene un atributo que es instancia de otra clase. Esta, posee el atributo se denomina
# “clase compuesta”, mientras que la clase a la cual pertenece el atributo de la clase
# compuesta se denomina “clase componente”.

# La composición es también llamada "agregación fuerte", siendo la agregación la interacción
# entre objetos donde una clase padre tiene una clase hija, como atributo de ella. En la
# composición, la clase padre corresponde a la clase compuesta, y la clase hija corresponde
# a la clase componente. 

# La diferencia entre la agregación “normal” y la agregación “fuerte” (composición), es que
# en la primera la instancia de la clase hija puede existir en forma independiente de su clase
# padre, en cambio, en la composición (agregación “fuerte”) la instancia específica del componente requiere
# necesariamente de la existencia de la clase compuesta para existir.

# Para condicionar que la instancia hija pueda existir en forma independiente de la instancia
# padre, se debe:

#       - dar al constructor de la clase padre una instancia de la clase hija como argumento.
#       - asignarlo a un atributo de instancia.

# De esta forma, se debe primero crear una instancia de la clase hija (es decir, puede existir
# por sí misma), que se usa como argumento para crear la clase padre.

# Recordar que Python no es estrictamente tipado, por lo que si no se indica el tipo de dato del atributo
# en el constructor, el uso de la agregación es difícil de deducir. 


#Agregación:

# class Material:
#     def __init__(self, nombre: str, duracion: str, textura: str):
#         self.nombre = nombre
#         self.duracion = duracion
#         self.textura = textura

# class Pelota:
#     def __init__(self, tamaño: int, color: str, material: Material) -> None:
#         self.tamaño = tamaño
#         self.color = color
#         self.material = material # La pelota tiene un material

# # El material existe en forma independiente de la pelota
# m = Material('Plástico', 'Corta', 'Lisa')
# p = Pelota(16, 'Amarillo', m)

# print(type(p.material)) # <class '__main__.Material'>
# print(p.material.nombre) # Plástico
# print(p.material.duracion) # Corta

# La clase Pelota tiene una referencia al objeto de la clase Material a través del atributo material.
# El objeto material puede existir independientemente de la pelota. En otras palabras, no se destruye 
# automáticamente cuando se destruye la pelota. Esto se ajusta a la definición de agregación, donde un 
# objeto contiene una referencia a otro objeto, pero ambos pueden existir por separado.
# Por lo tanto, en este caso, la relación entre Pelota y Material es de agregación. El objeto material 
# existe de manera independiente y puede ser compartido por varias pelotas si es necesario.


# Agregación “Normal”:
#   - En la agregación “normal”, también conocida simplemente como agregación, los objetos contenidos 
#     pueden existir de manera independiente de su objeto contenedor (clase padre).
#   - Los objetos contenidos no están vinculados de forma rígida al objeto contenedor.
#     Por lo tanto, si se destruye el objeto contenedor, los objetos contenidos no se destruyen automáticamente.
#     Ejemplo: Una universidad tiene profesores. Los profesores pueden existir incluso si la universidad no existe.

# Composición (Agregación “Fuerte”):
#   - En la composición (agregación “fuerte”), los objetos contenidos necesariamente requieren 
#     la existencia del objeto contenedor para existir.
#   - Los objetos contenidos están fuertemente vinculados al objeto contenedor.
#   - Si se destruye el objeto contenedor, todos los objetos contenidos se destruyen también.
#     Ejemplo: Un coche tiene ruedas. Las ruedas no pueden existir sin el coche.

# En resumen, la agregación permite una mayor flexibilidad, mientras que la composición garantiza una 
# relación más estrecha entre los objetos. Ambos conceptos son útiles en diferentes situaciones 
# de diseño de software.


# Composición en Python
# Para condicionar que una instancia hija no pueda existir por sí sola independiente de una
# clase padre, se debe:

#   - Crear la instancia de la clase hija (componente) dentro del constructor de la clase
#     padre (compuesto).
#   - Asignar esta instancia a un atributo, es decir, el componente no se debe usar como
#     argumento al momento de crear la instancia.

# Por lo tanto, la clase compuesta debe contener la información necesaria para crear la
# instancia de la clase componente dentro de su constructor.


# from abc import ABC, abstractmethod
# class Material(ABC):
#     @abstractmethod
#     def romper(self):
#         pass

# class MaterialPlastico(Material):
#     nombre = 'Plástico'
#     duracion = 'Corta'
#     def __init__(self, textura: str) -> None:
#         self.textura = textura
#     def romper(self):
#         pass

# class Pelota:
#     def __init__(self, tamaño: int, color: str, textura: str) -> None:
#         self.tamaño = tamaño
#         self.color = color
#         self.textura = textura
#         self.material = MaterialPlastico(self.textura) # La pelota está compuesta por un componente material

# p = Pelota(16, 'Rojo', 'Lisa')
# # Acceso a los atributos del material compuesto
# print(p.material.nombre) # Plastico
# print(p.material.duracion) # Corta
# print(p.material)


# La clase Pelota está creando una nueva instancia de MaterialPlastico dentro de su método __init__. 
# Esto significa que cada objeto Pelota tiene su propio objeto MaterialPlastico exclusivo.
# El ciclo de vida del objeto MaterialPlastico está completamente ligado al objeto Pelota. Si el objeto Pelota 
# se destruye, su objeto MaterialPlastico asociado también se destruirá.
# La composición implica que los objetos contenidos no pueden existir sin el objeto contenedor. 
# En este caso, el MaterialPlastico no puede existir sin la Pelota porque se crea dentro de la Pelota 
# y no tiene existencia independiente fuera de ella.