import personaje as p
import os
import sys
import time


class Juego:
    def __init__(self) -> None:
        clear = 'cls' if sys.platform == 'win32' else 'clear'
        os.system(clear)
        print('\n¡Bienvenido al Ataque del Orco!')
        print('-'*31)
        nombre_personaje = input('\nIngresa el nombre del héroe:\n> ')
        self.personaje = p.Personaje(nombre_personaje)
        self.orco = p.Personaje('Orco')

    def mostrar_estados(self):
        self.personaje.get_estado()
        self.orco.get_estado()

    def jugar(self):
        while True:
            print('\n¡Oh no!, ¡Ha aparecido un Orco\n')
            probabilidad_ganar = self.personaje.probabilidad_ganar(self.orco)
            print(p.Personaje.orco_visible(probabilidad_ganar))
            opcion = int(input('\n¿Qué deseas hacer?\n1. Atacar\n2. Huir\n>'))
            
            if opcion == 1:
                self.luchando(probabilidad_ganar)
            elif opcion == 2:
                print('¡Has huido! El orco ha quedado atrás...')
                time.sleep(1.5)
                print('\n*** Fin ***')
                break

    def luchando(self, probabilidad):
        print('Luchando con el Orco, espera...')
        time.sleep(2)
        print('...es una lucha difícil')
        time.sleep(1.3)
        os.system('cls' if sys.platform == 'win32' else 'clear')
        self.personaje.attack(probabilidad, self.orco)
        self.mostrar_estados()

if __name__ == "__main__":
    play = Juego()
    play.jugar()