import json
import time
from usuario import Usuario

archivo = 'usuarios.txt'
lista = []

def leer_archivo(archivo: str):
    arch = open(archivo, 'r')
    lines = arch.readlines()
    for line in lines:
        try:
            usuarios = json.loads(line) # aquí evalúo el error
        except Exception as e:
            with open('error.log', 'a') as log:
                log.write(f'ERROR: {e} - Time: {round(time.time())}\n')
        finally:
            nuevo_usuario = Usuario(usuarios.get('nombre'), usuarios.get('apellido'), usuarios.get('email'), usuarios.get('genero'))
            lista.append(nuevo_usuario)
            
    print(lista)

if __name__ == '__main__':
    leer_archivo(archivo)
