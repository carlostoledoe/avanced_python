import os
import random
import time

os.system('clear')

print('\n')
print('*** Juego: Los tesoros del duende maligno ***')
print('    =====================================')
print('\n')
print('Has entrado en una mansión abandonada con 4 habitaciones.')
print('En la mansión, está escondido un duende malvado que robará todos tu tesoros')
print('si te lo encuentras en una habitación y te quitará una de tus 2 vidas.')
print('\n')
print('Durante el juego tienes dos opciones: Entrar a una habitación y recoger un')
print('tesoro o, salir de la mansión con tus tesoros recogidos. Ten cuidado con')
print('el duende malvado, ya que robará todos tus tesoros.')
print('\n')
print('Recoge la máxima cantidad de tesoros y que la ambición no te mate!!!')
print('\n')

nombre = input('¿Cuál es tu nombre?: ')


inventario = []
vida = 2
dificultad = 6

def menu():
    print('\n')
    print('Elige una opción (ingresa el número): ')
    print('\n')
    print('1. Entrar al Comedor')
    print('2. Entrar al Baño')
    print('3. Entrar al Dormitorio')
    print('4. Entrar al sótano')
    print('0. Salir con tus tesoros econtrados')

def mostrar_inventario():
    print('\n')
    print(f'Te quedan: {vida} vidas')
    print(f'Tienes {len(inventario)} tesoro en tu inventario: ')
    print(inventario) 

def creditos():
    print('\n')
    print('Juego básico creado por Carlos Toledo para mostrar programación')
    print('a su sobrino Carlos Pavéz - 27/04/2024')
    print('*** FIN ****')

def muerte():
    os.system('clear')
    print(f'Ohhh! muy mala suerte {nombre} !!!')
    print('El duende te ha robado todo y matado...')
    print(f'Vuelve a intentarlo {nombre} !!')
    print('\n')
    creditos()
    exit()


def record():
    print('Tu record:')
    print(f'Recogiste: {len(inventario)} tesoros!! ')


while True:
    habitacion_duende = random.randint(1,dificultad)
    
    menu()
    opcion = int(input('Elige: '))
    print('Caminando hacia tu opción...')
    time.sleep(1.5)
    
    if opcion == habitacion_duende:
        os.system('clear')
        print('OH NO!!!!')
        print('Te has encontrado con el duende, te ha robado todo y quitado una vida...')
        vida = vida - 1
        if vida == 0:
            muerte()
        else:
            print('\n')
            print(f'Te quedan: {vida}')
            inventario = []
            mostrar_inventario()
        
    elif opcion == 1:
        os.system('clear')
        print(f'{nombre}, has entrado al Comedor y encontraste un diamante!!')
        inventario.append('Diamante')
        mostrar_inventario()
        
    elif opcion == 2:
        os.system('clear')
        print(f'{nombre}, has entrado al Baño y encontraste una Esmeralda!!')
        inventario.append('Esmeralda')
        mostrar_inventario()
        
    elif opcion == 3:
        os.system('clear')
        print(f'{nombre}, has entrado al Dormitorio y encontraste Oro!!')
        inventario.append('Oro')
        mostrar_inventario()
        
    elif opcion == 4:
        os.system('clear')
        print(f'{nombre}, has entrado al Sótano y encontraste un Ajedréz!!')
        inventario.append('Ajedréz')
        mostrar_inventario()
    
    elif opcion == 0:
        break



os.system('clear')

print('\n')
print(f'{nombre}, lograste salir de la masión!!!')
print('\n')

record()
creditos()