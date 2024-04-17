from tienda import Tienda
from producto import Producto

class Farmacia(Tienda):

    def Restoran(self):
        for p in self.productos:
                print(f'{p.nombre}, ${p.precio}')
    #socrescritura de método de la clase Tienda
    def ingresar_producto(self, nombre, precio):
        nuevo_producto = Producto(nombre, precio, 0)
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return 
        self.productos.append(nuevo_producto)