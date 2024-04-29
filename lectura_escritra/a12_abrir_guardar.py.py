# Open

# Carácter    Significado
# ’r’         abierto para lectura (por defecto)
# 'w'         abierto para escritura, truncando primero el fichero
# 'x'         abierto para creación en exclusiva, falla si el fichero ya existe
# ’a’         abierto para escritura, añadiendo al final del fichero si este existe
# 'b'         modo binario
# ’t’         modo texto (por defecto)
# ’+’         abierto para actualizar (lectura y escritura)

# # modo lectura (por defecto)
# archivo = open("ejemplo.txt")
# # modo lectura, espeficado por el segundo argumento 'r'
# historial = open("log.txt", 'r')



# Modo   Lee    Escribe  Crea-el-archivo Elimina-contenido
# 'r'     si        no           no             no
# 'r+'    si        si           no             no
# 'w'     no        si           si             si
# 'w+'    si        si           si             si
# 'a'     no        si           si             no
# 'a+'    si        si           si             no




# Opción 1:
# pagina = open('index.html')
# pagina.read() # Desde el terminal arroja: '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Document</title>\n</head>\n<body>\n    <h1>Hola Mundo!</h1>\n</body>\n</html>'


# Opción 2:
# pagina = open('index.html')
# lineas = pagina.readlines()
# print(lineas) 
# print(len(lineas)) # 11
# # Es una lista:
# # ['<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n', '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n', '    <title>Document</title>\n', '</head>\n', '<body>\n', '    <h1>Hola Mundo!</h1>\n', '</body>\n', '</html>']


# # Opción 3:
# with open('index.html', 'r') as archivo: # La declaración with se usa para manejar el archivo, lo que garantiza que el archivo se cierra automáticamente al final del bloque with, incluso si ocurre una excepción.
#     for linea in archivo: 
#         print(linea.strip()) # Cada linea leída del archivo incluye al final un carácter de nueva línea ('\n') o posibles espacios adicionales al principio o al final de la línea. El método linea.strip() se utiliza para eliminar estos caracteres de nueva línea y cualquier espacio en blanco extra antes de imprimir la línea.



# # Cerrar archivo 
# archivo = open("index.html")
# archivo.close()




# ¿Cómo abrir un archivo en modo de solo escritura?
# Si el archivo no existe, será creado sin contenido
# Si el archivo existe, se eliminará su contenido
# archivo = open('nuevo_log.log', 'w') # abierto para escritura, truncando primero el fichero




# # Escribiendo en un archivo:
# import time
# try:
#     edad = int(input('Ingrese su edad:\n'))
# except Exception as e:
#     with open(f'{round(time.time())}.log', 'w') as log: # Crea un archivo con la fecha
#         log.write(f'ERROR: {e}')








# # Modificar nombre archivo:
# import os
# # antiguo = os.path.join('logs', 'error.txt')
# # nuevo = os.path.join('logs', 'error.log')
# antiguo = 'error.txt'
# nuevo = 'error.log'
# os.rename(antiguo, nuevo)




# Para abrir un archivo que permita tanto su lectura como
# escritura (eliminando primero el contenido del archivo
# abierto), se debe entregar como segundo argumento de la
# función open (para el parámetro mode) el valor "r+".
# Este modo indica que el archivo se ha abierto para
# actualizar (permite lectura y escritura).
# Si el archivo entregado como primer argumento de open no
# existe, se lanzará una excepción de tipo FileNotFoundError.

# try:
#     edad = int(input("Ingrese su edad:\n"))
# except Exception as e:
#     with open("ultimo_error.log", "r+") as log: # No exisitía, error: FileNotFoundError. Luego de creado, eliminó el contenido
#         log.write(f"ERROR: {e}") 





# Append
# Puede usarse en combinación con el modo +, resultando el valor "a+"
# como segundo argumento de open. De esta forma, el archivo abierto
# también se puede leer. Si el archivo ingresado como primer argumento
# no existe, se crea.

# Al abrir un archivo ya sea en modo "a" o "a+", éste se abre apuntando “al
# final del documento”. Esto se logra por medio del método seek, el cual
# recibe como argumento la posición (en bytes, un número entero) donde
# se desea posicionar dentro del archivo. Al ingresar como argumento el
# valor 0, se posicionaría al comienzo del contenido.


# from datetime import datetime

# try:
#     edad = int(input("Ingrese su edad:\n"))
# except Exception as e:
#     with open("error.log", "a+") as log:
#         log.seek(0)
#         print(log.read())
#         now = datetime.now()
#         log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
#         log.seek(0)
#         print(log.read())




# # Lectura de bytes 
# with open("error.log") as log:
#     log.seek(10)
#     print(log.read(10))



# Al terminar la lectura de bytes indicadas, la posición de
# lectura del contenido se mueve al final de la cantidad de
# bytes indicada. 
# with open("error.log") as log:
#     log.seek(10)
#     print(log.read(10))
#     print(log.read(10))






# ¿Cómo leer un archivo completo por chunks de bytes?
# Existen ocasiones en que un archivo requiere ser manejado
# por bloques de lectura, a menudo debido a recursos
# limitados del computador frente a archivos de gran tamaño.
# A su vez, muchas veces este tipo de manejo coincide con la
# lectura de datos en modo binario, el cual se obtiene al
# agregar "b" en el modo de apertura. 

# chunk_size = 3
# with open("doc.pdf", "rb") as archivo:
#     chunk = archivo.read(chunk_size)
#     while chunk:
#         print(chunk)
#         chunk = archivo.read(chunk_size)






# En general, al trabajar con archivos, lo más importante es manejar correctamente su
# apertura y cierre. Es por eso que se recomienda:
#   - Siempre abrir archivos utilizando el context manager with, ya que de esta forma el
# archivo se cerrará en caso de ocurrir alguna excepción, o al llegar al final de su
# contenido.
#   - En lugar de usar with, envolver la apertura del archivo en un bloque try/finally, de forma
# que siempre se cierre el archivo con close dentro de finally











# "Generación de objetos a partir de un archivo"

# Se le solicita crear instancias de Producto a partir de los datos contenidos en un
# archivo de texto. Cada línea del archivo entregado corresponde a un texto en
# estructura json, donde cada clave corresponde al nombre de uno de los atributos de
# Producto, y el valor asociado a dicha clave corresponde al valor que debe poseer el
# atributo en la instancia.

# La estructura de la clase Producto es la siguiente:



# script productos.py
class Producto:
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

import json
instancias = []

with open('productos.txt') as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        instancias.append(Producto(producto.get('nombre'), producto.get('precio'))) 
        linea = productos.readline()

print(instancias)