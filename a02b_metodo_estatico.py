# Método estático
# Aquel que se puede llamar directamente desde la clase sin que se requiera una instancia. 
# Son como métodos generales. Son como una función, no requieren instancia
# Se define con el decorador @staticmethod, también dentro de su lógica no puede 
# modificar los valores de los atributos de la clase

# class Creature:
#     num_creatures = 0 
#     def __init__(self, name: str, health: int, power: int=100) -> None:
#         self.name = name
#         self.health = health
#         self.hp = health
#         self.power = power
#         self.bag = []
#         Creature.num_creatures += 1
    
#     @staticmethod
#     def show_num_creatures():
#         print(f'Se han creado {Creature.num_creatures} criaturas')
    
#     @staticmethod
#     def is_dead(creatire_hp):
#         return True if creatire_hp <= 0 else False
    
#     def attack(self, victim):
#         victim.hp -= self.power


# goro = Creature('Goro', 200, 80)
# kitana = Creature('Kitana', 100, 30)
# raiden = Creature('Raiden', 150, 60)
# reptile = Creature('Reptile',100, 40 )
# Creature.show_num_creatures() # Llamado a staticmethod


# #kitana atacka a raiden
# kitana.attack(raiden)
# print(f'La salud de raiden es {raiden.hp}')
# print(f'Está muerto? {Creature.is_dead(raiden.hp)}') # Llamado a staticmethod









# class Medicamento:
#     descuento = 0.05
#     iva = 0.18
    
#     @staticmethod
#     def validar_mayo_cero(numero: int): # Devuelve True o False
#         return numero > 0

# precio = int(input('Ingrese un precio a validar: \n'))
# es_valido = Medicamento.validar_mayo_cero(precio)

# print('El precio ingresado es valido') if es_valido else print("El precio ingresado no es válido")

# # Creamos dos intancias
# m1 = Medicamento()
# m2 = Medicamento()

# if m1.iva == m2.iva and m1.descuento == m2.descuento:
#     print('Ambas instancias tiene mismo IVA y descuento')
#     print('El valor del iva es: ', Medicamento.iva)
#     print('El valor del descuento es: ', Medicamento.descuento)











#Objetos
# Un objeto tiene características y acciones que realiza. Las características se denominan atributos,
# los cuales se definen dentro de la clase, y las acciones que realiza el objeto se definen en los métodos.



# class Medicamento():
#     descuento = 0.05
#     iva = 0.18
    
#     @staticmethod
#     def validar_precio(numero: int):
#         return numero > 0
    
#     def asignar_precio(self, precio: int):
#         es_valido = Medicamento.validar_precio(precio)
#         self.precio = precio if es_valido else print(f'El precio {precio} no es valido')

# med_nuevo = Medicamento()
# precio = int(input('Ingrese precio del medicamento: '))
# med_nuevo.asignar_precio(precio)
# print(f'El precio es medicamento ingreado es: {med_nuevo.precio}')





#Atributos de instancia o no estáticos
# Requieren necesariamente de una instancia de la clase u objeto, para poder acceder a 
# ellos o asignarles un valora. Son único para cada instancia

# class Pelota():
#     forma = 'redonda'
    
#     def asignar_color(self, nuevo_color: str):
#         self.color = nuevo_color
    
#     def mostrar_color_y_forma(self):
#         print('El color es {}'.format(self.color))
#         print('La forma es {}'.format(self.forma))
        

# pelota_nueva = Pelota()
# pelota_nueva.asignar_color('roja')
# pelota_nueva.mostrar_color_y_forma()
# pelota_nueva.forma = 'cuadrada' #problema
# pelota_nueva.mostrar_color_y_forma()









# class Medicamento():
#     descuento = 0.05
#     iva = 0.18
#     @staticmethod
#     def validar_precio(numero: int):
#         return numero > 0
#     def asignar_precio(self, precio_entregado: int):
#         es_valido = Medicamento.validar_precio(precio_entregado)
#         if es_valido:
#             self.precio = precio_entregado
#             self.descuento = 0
#         if 10000 <= self.precio < 20000:
#             self.descuento = 0.1
#         elif 20000 <= self.precio < 30000:
#             self.descuento = 0.2
#         elif self.precio >= 30000:
#             self.descuento = 0.3














# Cada orden de compra tiene un identificador (un código numérico)
# Total de productos
# Monto
# código de descuento: ""
# monto > 10000 "10PORCIENTO"
# monto > 20000 "20PORCIENTO"

# # orden_compra.py
# class OrdenDeCompra:
#     def nueva_orden(self):
#         self.identificador = 0
#         self.total_productos = 0
#         self.monto = 0
#     def asignar_monto(self, nuevo_monto: int):
#         self.monto = nuevo_monto
#         self.codigo_descuento = 'cero'
#         if nuevo_monto > 20000:
#             self.codigo_descuento = "20PORCIENTO"
#         elif nuevo_monto > 10000:
#             self.codigo_descuento = "10PORCIENTO"

# # generar_orden.py
# # from order_compra import OrdenDeCompra

# oc = OrdenDeCompra()
# oc.nueva_orden()

# oc.identificador = int(input('Ingrese el identificador de la OC: '))
# oc.total_productos = int(input('Ingrese el total de productos: '))
# oc.asignar_monto(int(input('Ingrese el monto: ')))
# print(f'El descuento es: {oc.codigo_descuento}')