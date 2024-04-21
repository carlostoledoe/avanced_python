# Método Constructor

# # Asignando valores directamente desde el cuerpo
# class Pelota:
#     def __init__(self) -> None:
#         self.color = 'Blanco'
#         self.tamaño = 20
#         self.material = 'Plástico'

# pupuple = Pelota()
# print(pupuple.color, pupuple.tamaño, pupuple.material)






# # Asignando valores desde parámetros
# class Pelota:
#     def __init__(self, color:str, tamaño = 20, material = 'Plástico') -> None:
#         self.color = color
#         self.tamaño = tamaño
#         self.material = material

# pupuple = Pelota('Verde', 16) # el tercer valor será tomado por defecto
# print(pupuple.color, pupuple.tamaño, pupuple.material)