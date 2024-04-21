from colorama import Fore, Back, Style, init

class DivError(Exception):
    pass

def div(num1: str, num2: str) -> str:
    try: 
        num1 = int(num1)
        num2 = int(num2)
        cousiente = num1 / num2 
    except ValueError as error:
        # debug(error)
        raise DivError('Debe ingresar solo numero enteros!')
    except ZeroDivisionError:
        raise DivError('No se puede dividir por cero')
    
    return 'El resultado de la división es: ' + str(cousiente)

def interact():
    while True:
        print(Style.RESET_ALL)
        num1 = input('Ingrese el dividendo o exit: ')
        if num1 == 'exit':
            break
        num2 = input('Ingrese el divisor: ')
        
        try:
            result = div(num1, num2)
            print(result)
        except DivError as e:
            print(Fore.RED + Back.BLACK, e)

interact()