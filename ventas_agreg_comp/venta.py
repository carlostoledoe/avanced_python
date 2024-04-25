class DetalleVentaItem:
    def __init__(self, producto: str, cantidad: int) -> None:
        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

class DetalleVenta:
    def __init__(self) -> None:
        self._items = []
    
    def agregar_item(self, item: DetalleVentaItem): # Agregación: 
        # DetalleVentaItem se agrega una vez ya creada la instancia 
        # DetalleVenta. Es decir, DetalleVentaItem existe de forma 
        # independiente de DetalleVenta (se crea dentro de Venta).
        # Por lo tanto, la relación de estas clases es de agregación, 
        # siendo DetalleVenta la clase padre, y DetalleVentaItem la 
        # clase hija.
        # los objetos contenidos (DetalleVentaItem) pueden existir de manera independiente
        # de su objeto contenedor (clase padre DetalleVenta)
        self._items.append(item)
    
    def __str__(self) -> str:
        retorno = (':::::::: DETALLE DE ESTA VENTA :::::::::\nPRODUCTO\tCANTIDAD\n')
        items = [ f'{i.producto}\t\t{i.cantidad}\n' for i in self._items ]
        return f'{retorno}{"".join(items)}'

class Venta:
    def __init__(self) -> None:
        self._detalle = DetalleVenta() # Composición: La instancia de DetalleVenta
        # se crea dentro del constructor de Venta y está completamente
        # integrada en la estructura de Venta. Si eliminamos una instancia
        # de Venta, también se eliminará la instancia de DetalleVenta
        # Tiene un atributo que es instancia de otra clase. 
        # Una clase padre (Venta) tiene una clase hija (DetalleVenta), como
        # atributo de ella. En la composición, la clase padre corresponde
        # a la clase compuesta, y la clase hija corresponde a la clase 
        # componente. 
    
    def modificar_detalle(self, producto: str, cantidad: str):
        detalle_venta_item = DetalleVentaItem(producto, cantidad) # Colaboración:
        # Que una clase colabore con otra,quiere decir que una clase 
        # debe ser instanciada dentro de la otra. Los objetos que forman
        # parte de una colaboración no dependen uno del otro para existir.
        # Para que exista una Venta, no es necesario que posea un DetalleVentaItem; 
        # solo lo requiere para realizar la acción de agregar ítems al detalle.
        # Por lo tanto, la relación de estas clases es de colaboración, donde
        # DetalleVentaItem colabora con Venta para agregar un ítem a su detalle.
        self._detalle.agregar_item(detalle_venta_item) 
    
    @property
    def detalle(self):
        return self._detalle