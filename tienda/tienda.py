from producto import Producto

# tipo = "supermercado" | "farmacia" | "restoran"
# Luego, modelarlo con clase abstracta, sobreescribir 
# los métodos dependiendo que clase estoy instanciando


class Tienda:
    def __init__(self, nombre, costo_delivery, tipo):
        self._nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []
        self.tipo = tipo    

    def ingresar_producto(self, producto, nombre, precio, stock):
        self.productos.append(producto)
        nuevo_producto = Producto(nombre, precio, stock)
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return 
            # si llego, significa que quiere decir que nunca encontró el producto
            self.productos.append(nuevo_producto)

    def listar_productos(self):
        pass

    def realizar_venta(self):
        pass