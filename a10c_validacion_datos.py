# Usted forma parte de una empresa que se encuentra desarrollando una aplicación
# de calendario y agenda. Se le ha solicitado, mediante una aplicación de consola
# Python, crear un pequeño demo que ejecute el algoritmo para validar el ingreso de
# los datos necesarios para crear una reunión previo a crearla. Por ahora se le pide
# que considere que una reunión debe tener los siguientes atributos y validaciones:

# - Título: Cadena de texto. No puede tener más de 150 caracteres.
# - Hora: Cadena de texto. El contenido debe estar en formato “HH:MM:SS”.

# Desde su empresa le han solicitado que maneje las validaciones de datos
# ingresados mediante uso de excepciones propias.












# En archivo error.py
class Error(Exception): # Clase Base Exepciones
    pass

class HoraError(Error):
    pass

class LargoTextoError(Error):
    # Sobreescriba el constructor, admitiendo los parámetros mensaje, texto (opcional)
    # y largo (opcional), los cuales debe asignar a atributos de instancia. En el caso
    # del texto, acortar en caso de que supere los 50 caracteres
    def __init__(self, mensaje: str, texto: str = None, largo: int = None) -> None:
        self.mensaje = mensaje
        self.texto = (f'{texto[50]}...' if texto is not None and len(texto) > 50 else texto)

    def __str__(self) -> str:
        # sobrecargue el método __str__. En caso de que no se haya ingresado texto ni 
        # largo, retornar el método de la clase padre. En caso contrario, según los
        # valores ingresados, construir mensaje de retorno.
        if self.texto is None and self.largo is None:
            return super().__str__()
        else:
            mensaje_ret = f'{self.mensaje}'
            if self.texto != None:
                mensaje_ret += f' Texto ingresado: {self.texto}.'
            if self.largo != None:
                mensaje_ret += f' Máximo {self.largo} carácteres permitidos.'
            return mensaje_ret

# En archivo reunion.py
class Reunion:
    def __init__(self, titulo: str, hora: str) -> None:
        self.titulo = titulo
        self.hora = hora

# En archivo demo.py
# from error import HoraError, LargoTextoError
# from reunion import Reunion
import re # Para trabajar con expresiones regulares (regex)

titulo = None
hora = None
#time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"
time_re = "^([01]?\\d|2[0-3]):([0-5]?\\d):([0-5]?\\d)$"

# Iniciar un ciclo while infinito y dentro de este crear un bloque try/except. La cláusula
# except debe manejar todas las excepciones de tipo Exception. En ella, mostrar la
# instancia de la excepción y agregar la instrucción continue. Agregar también una
# cláusula else, y en ella agregar la instrucción break.

# Dentro de la cláusula try, solicitar el título, en caso de que este no tenga valor
# o su largo supere 150. Luego de ser ingresado, en caso de que su largo sea superior
# a 150, lanzar una excepción de tipo LargoTextoError.

while True:
    try:
        if titulo is None or len(titulo) > 20:
            titulo = input('\nIngrese título de la reunión\n(Máximo 20 carácteres):')
        if len(titulo) > 20:
            raise LargoTextoError('Título de la reunión exede máximo de carácters', titulo, 20)
        if hora is None or re.search(time_re, hora) is None:
            hora = input('\nIngrese hora de la reunión\n(Formato: HH:MM:SS):\n')
            if re.search(time_re, hora) is None:
                raise HoraError('Formato de hora debe ser HH:MM:SS')
    except Exception as e:
        print(f'\nEl error es: {e}\n')
        continue
    else:
        break

r = Reunion(titulo, hora)
print('\nReunión creada correctamente')
