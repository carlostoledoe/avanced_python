from tienda import Tienda

class Supermercado(Tienda):
    def listar_productos(self):
        for p in self.productos:
            if p.stock <= 10:
                print(f'{p.nombre}, ${p.precio}, Unidades: {p.stock} Pocas unidades disponibles')
            else:
                print(f'{p.nombre}, ${p.precio}, Unidades: {p.stock}')

if __name__ == '__name__':
    m = Supermercado('Ekono', 1500)
    m.ingresar_producto('Atún', 1300, 300)
    m.ingresar_producto('Papél higénico', 5000, 8)
    print(m.productos)
    m.listar_productos()

