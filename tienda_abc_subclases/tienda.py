# tipo = "supermercado" | "farmacia" | "restoran"
'''
- Restoran al momento de agregar productos, el stock 
siempre es 0
- Al momento de listar los restaurante y farmacia 
esconden el stock
- Supermercados muesran mensaje pocos disponible si el
stock es <= 10
- Las farmacias agregan envio gratis si el precio es
superior a 15000
'''
from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):

    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        for prod in self.productos:
            if prod == nuevo_producto: # Si lo encientra, entonces
                prod.stock += nuevo_producto.stock # Le agrega el nuevo stock del producto
                return 
        self.productos.append(nuevo_producto) # Si llega aquí, el producto no se encontró, por lo tanto se agrega

    @abstractmethod 
    def listar_productos(self): # Es distinto para sup, rest y farmacia.Está para ser una clase abstracta
        pass  

    def realizar_venta(self, nombre_bucado, cantidad_solicitada):
    
        for producto in self.productos:
            if producto.nombre == nombre_bucado and producto.stock >= cantidad_solicitada:
                print(f'Se vende {cantidad_solicitada} unidades del producto {producto.nombre}')
                producto.stock -= cantidad_solicitada
                return
        # si llegamos acá, el producto no existe o no hay stock suficiente
        print(f'No hay suficientes {nombre_bucado}')