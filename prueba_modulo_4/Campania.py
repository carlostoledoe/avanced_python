from Anuncio import Anuncio

class Campania:
    def __init__(self, nombre:str, fecha_inicio, fecha_termino) -> None:
        anuncio = Anuncio()
        lista_anuncio = []

        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        lista_anuncio.append(anuncio)

    def __str__(self):
        pass