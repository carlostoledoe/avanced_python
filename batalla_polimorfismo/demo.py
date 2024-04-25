from jugador import Jugador
from monstruo import Monstruo

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
orco = Monstruo(200, 12, 5)

print('Bienvenidos al juego!\n')
opcion = None
while opcion is not '0':
    print('\n>>> Interacción <<<<')
    
    ataque = heroe.ataque()
    print(f'Heroe ataca: {ataque}')
    orco.defensa(ataque)
    print('Orco se defiende...')
    print(f'HP Heroe {heroe.hp}')
    print(f'HP Orco {orco.hp}')
    
    print('\n')
    
    ataque = orco.ataque()
    print(f'Orco ataca: {ataque}')
    heroe.defensa(ataque)
    print('Heroe se defiende...')
    print(f'HP Heroe {heroe.hp}')
    print(f'HP Orco {orco.hp}')
    if orco.hp < 0 or heroe.hp < 0:
        break
    opcion = input('¿Desea continuar?\n>')
print('Ha muerto un luchador, fin') 