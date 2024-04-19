
class Fotos:
    def __init__(self, imagen: str, ancho, alto: str):
        self.__imagen = imagen
        self.__ancho = ancho
        self.__alto = alto
        self.__reacciones = 0

    @property
    def _imagen(self):
        return self.__imagen

    @_imagen.setter
    def _imagen(self, value):
        self.__imagen = value

    @property
    def _ancho(self):
        return self.__ancho

    @_ancho.setter
    def _ancho(self, value):
        self.__ancho = value

    @property
    def _alto(self):
        return self.__alto

    @_alto.setter
    def _alto(self, value):
        self.__alto = value

    @property
    def _reacciones(self):
        return self.__reacciones

    @_reacciones.setter
    def _reacciones(self, value):
        self.__reacciones = value


class FotoPerfil(Fotos):
    def __init__(self, imagen, ancho, alto):
        super().__init__ (imagen, ancho, alto) #llamamos la contructor de la clase madre
        recorte = [(0,0), (0, alto), (ancho, 0), (ancho, alto)]
