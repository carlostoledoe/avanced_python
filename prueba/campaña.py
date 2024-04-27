from anuncio import Anuncio
from dataclasses import date
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date) -> None:
        # listado_anuncios = []

        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino

        @fecha_inicio.setter
        def fecha_inicio(self, value):
            self.__fecha_inicio = value

        @fecha_termino.setter
        def fecha_termino(self, value):
            self.__fecha_termino = value

        # anuncio = Anuncio()
        # listado_anuncios.append(anuncio)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if len(self.__nombre) > 250:
            raise LargoExcedidoException('Error: Subtipo no permitido!')
        self.__nombre = value

    def __str__(self):
        pass
