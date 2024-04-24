# Guardar errores 
import time
try:
    edad = int(input('Ingrese números:\n'))
except Exception as e:
    with open('error.log', 'a') as log:
        log.write(f'ERROR: {e} - Time: {round(time.time())}\n')




