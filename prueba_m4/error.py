class Error(Exception):
    pass

class SubTipoInvalidoException(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje


class LargoExcedidoException(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje
