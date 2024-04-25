# Compimir anuncio es abstracto
# redimensionar_anuncio es abtracto
# mostrar_formato es estatico

from abc import ABC, abstractmethod

class Anuncio(ABC):

    sub_tipos = ()

    def __init__(self, ancho: int, alto: int, url_archivo:str, url_clic:str, sub_tipo:str) -> None:

        self._ancho = ancho if ancho > 0 else 1
        self._alto = alto if alto > 0 else 1

        self._url_archivo = url_archivo
        self._url_clic = url_clic

        self._sub_tipo = sub_tipo

        if self.sub_tipo not in self.sub_tipos:
            raise SubTipoInvalidoError    

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        self._ancho = value

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        self._alto = value             
        
    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if self.sub_tipo not in self.sub_tipos:
            raise SubTipoInvalidoError
        else:
            self._sub_tipo = value            

            
    @staticmethod
    def mostrar_formatos():
        pass

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass


class SubTipoInvalidoError(Exception):
    def __init__(self, sub_tipo):
        self.sub_tipo = sub_tipo

    def __str__(self):
        return f'{self.sub_tipo} no es un tipo valido para esta opcion'