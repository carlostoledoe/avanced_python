# 1. Errores de sintaxis -> Programa no funciona
# 2. Errores de ejecución -> Programa funciona pero se detiene en algún punto

#  ----- Excepciones ------

# JUEGO DE DADOS
# Crear una clase especial para las excepciones de este tipo de objetos (InvalidDiceError)
# Crear una clase para el juego de dados que contiene:
# Lanzamiento de dados
# juego
import random

class Error(Exception):
  pass

class InvalidDiceError(Error):
  def __init__(self, mensaje, numero):
    self.__mensaje = mensaje
    self.__numero = numero

    @property
    def mensaje(self):
      return self.__mensaje
    
    @property
    def numero(self):
      return self.__numero

class JuegoDado:
  def __init__(self) -> None:
    self.__dados = {
      4: 'D4',
      6: 'D6',
      8: 'D8',
      10: 'D10',
      12: 'D12',
      20: 'D20'
    }
  def lanzamiento(self, caras, tiradas):
    if caras not in self.__dados:
      raise InvalidDiceError(f'El dado {caras} no existe', caras)
    return [random.randint(1, caras) for _ in range(tiradas)]
  '''
  El try puede tener entre 2 y 4 partes:
  try (intentará hacer)
  varios expect (los capturar el except)
  finally (block ocurren cosas despues de que pasó el try y except)
  else (si no pasa nada)
  '''
  def game(self):
    while True:
      try:
        print('Opciones de dados:')
        for lados in self.__dados:
          print(f'{lados}-caras : {self.__dados[lados]}')
        caras = int(input('Ingrese el numero de caras del dado: '))
        tiradas = int(input('Ingrese el numero de tiradas: '))
        resultado = self.lanzamiento(caras, tiradas)
      except InvalidDiceError as e: 
        print(e)
        print(f'El resuldado de {self.__dados[caras]} es {resultado}')
      except ValueError:
        print('Error: El valor ingresado no es un numero')
      except Exception as e:
        print(f'Error: {e}')
      finally:
        try:
          respuesta = input('¿Desea continuar? (s/n): ')
          if respuesta.lower() != 's':
            print('Gracias por jugar')
        except Exception as e:
          print(f'Error: {e}')

if __name__ == '__main__':
  juego = JuegoDado()
  juego.game()