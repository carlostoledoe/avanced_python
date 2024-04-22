# Creación, eliminación y representación de objetos        __init__, __del__, __str__
# Acceso a atributos                                       __getattr__, __setattr__
# Atributos del descriptor                                 __get__, __set__, __delete__
# Secuenciar y mapear objetos                              __len__, __getitem__, __contains__
# Iteración                                                __iter__
# Operaciones matemáticas                                  __add__, __pow__, __int__
# Comparaciones                                            __lt__, __eq__, __ne__
# Llamado de objetos                                       __call__


# # str
# class Persona:
#     def __str__(self) -> str: # Necesariamente debe ser un string el retorno
#         return 'Método str sobrescrito'

# juan = Persona()
# print(juan) # Sin sobrescritura: <__main__.Persona object at 0x7f67ee65b490>








# class Pelota:
#     def __init__(self, tamaño: int = 0) -> None:
#         self.tamaño = tamaño
#     def __add__(self, otra_pelota):
#         return self.tamaño + otra_pelota.tamaño

# p1 = Pelota(25)
# p2 = Pelota(33)
# print(p1 + p2) # 58, en caso de no estar : TypeError: unsupported operand type(s) for +: 'Pelota' and 'Pelota'






# # Suma
# class Coordenada:
#     def __init__(self, x = 0, y = 0) -> None:
#         self.x = x
#         self.y = y
#     def __add__(self, otro):
#         nuevo_x = self.x + otro.x
#         nuevo_y = self.y + otro.y
#         return Coordenada(nuevo_x, nuevo_y)

# c1 = Coordenada(5, 10)
# c2 = Coordenada(-5, 10)
# suma_coordenadas = c1 + c2 
# print(type(suma_coordenadas)) # <class '__main__.Coordenada'>
# print(f'{suma_coordenadas.x}, {suma_coordenadas.y}') # 0, 20









# # eq
# class Pelota:
#     def __init__(self, tamaño = 0):
#         self.tamaño = tamaño

# p1 = Pelota(16)
# p2 = Pelota(16)
# p3 = p2

# print(p1 == p2) # False, porque son dos objetos diferentes en memoria
# print(p2 == p3) # True, xq son el mismo objeto en la memoria









# class Pelota():
#     def __init__(self, tamaño = 0):
#         self.tamaño = tamaño
#     def __eq__(self, other):
#         return self.tamaño == other.tamaño


# p1 = Pelota(16)
# p2 = Pelota(16)

# print(p1 == p2) # True











# class Balon():
#     def __init__(self, tamaño = 0) -> None:
#         self.tamaño = tamaño
#     def __eq__(self, otro: object) -> bool:
#         if not isinstance(otro, Balon):
#             # No intentes comparar una Pelota con un objeto que no es una Pelota
#             return NotImplemented
#         return self.tamaño == otro.tamaño

# p1 = Balon(16)
# p2 = Balon(16)
# p3 = p2

# print(p1 == p2) # Ahora esto debería dar True
# print(p2 == p3) # Esto sigue dando True










# # __eq__ ==        __iadd__ +=
# class Medicamento():
#     IVA = 0.18
#     def __init__(self, nombre: str, stock):
#         self._nombre = nombre
#         self._stock = stock
#     def __eq__(self, other): # Comparación
#         return self._nombre.lower() == other._nombre.lower()
#     def __iadd__(self, other): # Modifica el += 
#         if self == other:
#             self._stock += other._stock
#         return self

# m1 = Medicamento('PARACETAMOL', 10)
# m2 = Medicamento('Aspirina', 5)
# m3 = Medicamento('PaRACetaMOl', 15)

# print(m1 == m2) #False
# print(m1 == m3) #True
# m1 += m2 # 10, al ser diferente, matiene el stock
# print(m1._stock)
# m1 += m3
# print(m1._stock) # 25













#archivo medicamento.py 
class Medicamento():
    IVA = 0.18
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    @property
    def precio(self):
        return self.precio_final
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA
        if self.precio_final >= 10000 and self.precio_final < 20000:
            self.descuento = 0.1
        elif self.precio_final >= 20000:
            self.descuento = 0.2
        if self.descuento:
            self.precio_final *= 1 - self.descuento
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self

# archivo programa.py
# from medicamento import Medicamento
opcion_ingreso = int(input("¿Desea agregar un medicamento? \n1. Sí\n2. No\n"))
ingresados = []

while opcion_ingreso == 1: #opción si anterior
    nombre = input("\nIngrese nombre del medicamento: ")
    stock = int(input("\nIngrese stock del medicamento: "))
    m = Medicamento(nombre, stock) # Crea una instancia
    if m in ingresados: # Si la instancia está en ingreados,
        indice = ingresados.index(m) # obtiene el indice
        ingresados[indice] += m #suma el stock la la instancia del indice
    else:
        indice = 0
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento: "))
        m.precio = precio_bruto

    print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
    print(f"PRECIO FINAL: ${m.precio_final}")
    
    stock = ingresados[indice].stock if len(ingresados) > 0 else m.stock
    print(f"STOCK: {stock}")
    
    print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    
    opcion_ingreso = int(input("¿Desea agregar un medicamento? \n1. Sí\n2. No\n"))
print('Saliendo...')






