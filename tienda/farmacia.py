from tienda import Tienda

class Farmacia(Tienda):
    def listar_productos(self):
        for p in self.productos:
            if p.precio > 15000:
                print(f'{p.nombre}, ${p.precio} Envio Gratis')
            else:
                print(f'{p.nombre}, ${p.precio}')
                
    def realizar_venta(self, nombre_bucado, cantidad_solicitada):
        if (cantidad_solicitada > 3):
            print('Por ley, no podemos vender más de 3 unidades')
            return
        super().realizar_venta(nombre_bucado, cantidad_solicitada)

if __name__ == '__name__':
    salco = Farmacia('Dr. Simi', 10000)
    salco.ingresar_producto('Panadol', 16000, 300)
    salco.ingresar_producto('Aspirina', 5000, 8)
    print(salco.productos)
    salco.listar_productos()