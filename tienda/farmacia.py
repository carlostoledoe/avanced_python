from tienda import Tienda

class Farmacia(Tienda):

    def listar_productos(self):
        for p in self.productos:
            if p.precio > 15000:
                print(f'{p.nombre}, ${p.precio} Envio Gratis')
            else:
                print(f'{p.nombre}, ${p.precio}')


salco = Farmacia('Dr. Simi', 10000)
salco.ingresar_producto('Panadol', 16000, 300)
salco.ingresar_producto('Aspirina', 5000, 8)
print(salco.productos)
salco.listar_productos()