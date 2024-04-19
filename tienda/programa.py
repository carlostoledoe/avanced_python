import sys
from farmacia import Farmacia
from supermercado import Supermercado
from restoran import Restoran

if __name__ == '__main__':
    resp = input('Qué desea crear: \n1. Farmacia\n2. Supermercado\n3. Restaurante:\n')
    nombre = input('Ingrese el nombre:\n')
    costo_delivery = int(input('Ingrese el costo del devilvery:\n'))
    
    tienda = None
    
    if resp == '1':
        tienda = Farmacia(nombre, costo_delivery)
    elif resp == '2':
        tienda = Supermercado(nombre, costo_delivery)
    elif resp == '3':
        tienda = Restoran(nombre, costo_delivery)
    else:
        print('Ese tipo de tienda no exite')
        sys.exit(2)
    
    while True:
        nombre = input('Ingrese el nombre del producto, o 0 para terminar\n')
        if nombre == '0':
            break
        precio = int(input('Ingrese el precio del producto\n'))
        stock = int(input('Ingrese el stock disponible\n'))
    
        tienda.ingresar_producto(nombre, precio, stock)
    
    print('Estos son los detalles de su tienda:')
    tienda.listar_productos()
