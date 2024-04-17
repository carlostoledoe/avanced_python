from producto import Producto

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

class Tienda:

    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return 
        self.productos.append(nuevo_producto)

    def listar_productos(self):
        pass

    def realizar_venta(self):
        pass