class Producto: # Entidad debil, xq la tienda
    def __init__(self, nombre, precio, stock = 0):
        self.nombre = nombre
        self.precio = precio
        if stock < 0:
            self.stock = 0
        else:
            self.stock = stock

def __eq__(self, otro_prod): # ==
    return self.nombre == otro_prod.nombre
