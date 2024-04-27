from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def _ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self.__url_archivo = value

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value):
        self.__url_clic = value

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        self.__sub_tipo = value
        # Al querer modificar el sub_tipo de algún anuncio ya creado, se debe validar que se
        # esté ingresando un subtipo dentro de los permitidos en el tipo de la instancia actual.
        # Los subtipos permitidos para las instancias de cada clase corresponden a los
        # elementos de la tupla definida en el atributo de clase SUB_TIPOS respectivo. En caso
        # de no cumplirse esta condición al momento de querer cambiar el valor del atributo
        # sub_tipo, se debe lanzar una excepción SubTipoInvalidoException.

    @staticmethod
    def mostrar_formatos():
        pass

    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    formato = 'Video'
    sub_tipos = ('instream', 'outstream')
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        ancho_fijo = 1
        alto_fijo = 1
        super().__init__(ancho_fijo, alto_fijo, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5

    def mostrar_formmato(formato, sub_tipos):
        if sub_tipos not in Video.sub_tipos:
            raise SubTipoInvalidoException('Error: Subtipo no permitido!')
        sub_tipo1, sub_tipo2 = sub_tipos
        print(f'{Video.formato}\n===========\n- {sub_tipo1}\n- {sub_tipo2}')

    def comprimir_anuncio(self):
        return print('COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        return print('RECORTE DE VIDEO NO IMPLEMENTADO AÚN')

class Display(Anuncio):
    formato = 'Display'
    sub_tipos = ('tradicional', 'native')
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def mostrar_formmato(formato, sub_tipos):
        if sub_tipos not in Video.sub_tipos:
            raise SubTipoInvalidoException('Error: Subtipo no permitido!')
        sub_tipo1, sub_tipo2 = sub_tipos
        print(f'{Video.formato}\n===========\n- {sub_tipo1}\n- {sub_tipo2}')

    def comprimir_anuncio(self):
        return print ('COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        return print ('REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN')

class Social(Anuncio):
    formato = 'Social'
    sub_tipos = ('facebook', 'linkedin')
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def mostrar_formmato(formato, sub_tipos):
        if sub_tipos not in Video.sub_tipos:
            raise SubTipoInvalidoException('Error: Subtipo no permitido!')
        sub_tipo1, sub_tipo2 = sub_tipos
        print(f'{Video.formato}\n===========\n- {sub_tipo1}\n- {sub_tipo2}')
    
    def comprimir_anuncio(self):
        return print('COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        return print('REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN')