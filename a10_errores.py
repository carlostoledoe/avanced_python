# from colorama import Fore, Back, Style, init

# class DivError(Exception):
#     pass

# def div(num1: str, num2: str) -> str:
#     try: 
#         num1 = int(num1)
#         num2 = int(num2)
#         cousiente = num1 / num2 
#     except ValueError as error:
#         # debug(error)
#         raise DivError('Debe ingresar solo numero enteros!')
#     except ZeroDivisionError:
#         raise DivError('No se puede dividir por cero')
    
#     return 'El resultado de la división es: ' + str(cousiente)

# def interact():
#     while True:
#         print(Style.RESET_ALL)
#         num1 = input('Ingrese el dividendo o exit: ')
#         if num1 == 'exit':
#             break
#         num2 = input('Ingrese el divisor: ')
        
#         try:
#             result = div(num1, num2)
#             print(result)
#         except DivError as e:
#             print(Fore.RED + Back.BLACK, e)

# interact()







# # Guardar errores 
# import time
# try:
#     edad = int(input('Ingrese números:\n'))
# except Exception as e:
#     with open('error.log', 'a') as log:
#         log.write(f'ERROR: {e} - Time: {round(time.time())}\n')












# #Valor no valido o error
# secreto = 3
# while True:
#     try:
#         numero = int(input('Adivina el número: '))
#         if numero == secreto:
#             break
#         else:
#             print('> Numero erroneo. Itenta de nuevo.')
#     except ValueError: 
#         print('> Eso no es un número. Intenta de nuevo.')
# print ('Correcto!!')










# # En caso que ingrese un string
# try: 
#     eleccion = int(input('Elija un número: '))
# except ValueError:
#     print(f'Debe ingresar solo números')
# else:
#     print(f'Correcto, ha eledigo el número {eleccion}')
