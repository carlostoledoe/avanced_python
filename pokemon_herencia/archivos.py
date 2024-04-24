import json
from pokemon import Pokemon

archivo = 'guardados.txt'

pokemones = []

def leer_pokemones():
    # 1. abrir el archivo
    arch = open(archivo, 'r')
    # 2. Leemos el contenido
    # pokemones = arch.read() # Lee todo el contenido
    lines = arch.readlines()
    for line in lines:
        line = line.replace('\n', '')
        pokemon = json.loads(line)
        pokemones.append(pokemon)
        
    # 3. Cerrar el archivo
    arch.close()
    # 4. Print
    print(type(pokemones))
    print(pokemones)

def guardar_pokemones():
    # 1. Abrimos el archivo
    arch = open(archivo, 'w') # piso el contenido anterior
    
    # 2. Escribimos una a una las líneas de texto
    # arch.write('Pikachu, 100, Normal\n')
    # arch.write('Buterflu, 200, Insecto\n')
    # arch.write('Charizar, 100, Fuego\n')
    
    # 2. Creamos los pokemones somo string (Json)
    # p1 = json.dumps({
    # 'name': 'Pikachu',
    # 'health': 100,
    # 'type': 'normal'
    # }) + '\n'
    
    # p2 = json.dumps({
    # 'name': 'Buterfly',
    # 'health': 200,
    # 'type': 'insecto'
    # }) + '\n'
    
    # p3 = json.dumps({
    # 'name': 'Charizar',
    # 'health': 150,
    # 'type': 'fuego'
    # }) + '\n'
    
    # arch.write(p1)
    # arch.write(p2)
    # arch.write(p3)
    for pokemon in pokemones:
        poke_str = json.dumps(pokemon) + '\n'
        arch.write(poke_str)
    # 3. Cerramos el archivo
    arch.close()

def crear_pokemon():
    name = input('Elija un nombre: ')
    health = int(input('Elija salud '))
    type = input('Elija un tipo: ')
    pokemones.append({
        'name': name,
        'health': health,
        'type': type
    })

def listar_pokemones():
    print(pokemones)



if __name__ == '__main__':
    #guardar_pokemones()
    leer_pokemones()
    
    while True:
        eleccion = input('Elija una opción para sus Pokemones:\n\n1. Crear Pokemon\n2. Mostrar Pokemon\n3. Guardar Pokemones\n0. Salir\n')
        if eleccion == '1':
            crear_pokemon()
        elif eleccion == '2':
            listar_pokemones()
        elif eleccion == '3':
            guardar_pokemones()
        elif eleccion == '0':
            break
        else:
            print('Operación no permitida')
