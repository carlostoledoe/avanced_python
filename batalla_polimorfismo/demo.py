from jugador import Jugador
from monstruo import Monstruo
import os
import sys

# enfrentados = [Jugador(500, 10, 5, "espada"), Monstruo(500, 5, 8)]
# atk = 0
# print(type(enfrentados))

# while any(e.hp <= 0 for e in enfrentados) == False:
#     for e in enfrentados:
#         if atk:
#             e.defensa(atk)
#         if e.hp > 0:
#             atk = e.ataque()
#             print(f'{e.__class__.__name__}: HP: {e.hp}')
#             print(f'{e.__class__.__name__}: ATK: {e.atk}\n')
#         else:
#             print(f"¡Oh no!, el {e.__class__.__name__} ha muerto :(")


heroe = Jugador(200, 10, 5, "espada")
orco = Monstruo(200, 10, 5)

os.system('cls' if sys.platform == 'win32' else 'clear')
print('Bienvenidos al juego!\n')
opcion = None
while opcion != '0':
    print('\n>>> Interacción <<<<')
    
    ataque = heroe.ataque()
    print(f'Heroe ataca: {ataque}')
    orco.defensa(ataque)
    
    print(f'''Orco se defiende...
    HP Heroe: {heroe.hp}
    HP Orco: {orco.hp}\n''')
    
    ataque = orco.ataque()
    print(f'Orco ataca: {ataque}')
    heroe.defensa(ataque)
    
    print(f'''Heroe se defiende...
    HP Heroe: {heroe.hp}
    HP Orco: {orco.hp}\n''')
    
    if orco.hp < 0:
        print('Ha muerto el Orco!')
        break
    elif heroe.hp < 0:
        print('Ha muerto el Heroe!')
        break
    opcion = input('¿Desea continuar? (Si: ENTER, No: 0)\n>')
print('FIN')