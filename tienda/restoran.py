from tienda import Tienda
from producto import Producto

class Restoran(Tienda):

    def listar_productos(self):
        for p in self.productos:
                print(f'{p.nombre}, ${p.precio}')
    
    #socrescritura de método de la clase Tienda
    def ingresar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, 0)
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return 
        self.productos.append(nuevo_producto)
    
    def realiza_venta(self, nombre_buscado, cantidad_solicitada= None):
        for prod in self.producto:
            if prod.nombre == nombre_buscado:
                print(f'Sale un {nombre_buscado} maestro')
                return
            print('Ese plato no lo trabajamos')