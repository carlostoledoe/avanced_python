# # Errores durante la ejecución del código 'excepciones'
# nombre = 'Hola'
# apellido = 'Chao'
# print(nombre / apellido) 
# # TypeError: unsupported operand type(s) for /: 'str' and 'str'





# # Errores que impiden que el programa se ejecute "errores de sintaxis"
# def metodo();
# pass
# # SyntaxError: expected ':'



# # Errores lógicos, resulados inpesperados:
# num1 = input('Ingrese primer número: ') # 13
# num2 = input('Ingrese segundo número: ') # 22
# print(num1 + num2) #1322



# Qué es una exepción:
# - Corresponde a un error de ejecución, el cual tiene un tipo asociado.
# - El tipo de la excepción corresponde al nombre de la clase de la excepción, lo cual es
#   válido para todas las excepciones predefinidas por el intérprete de Python (conocidas 
#   como excepciones built-in).
# - También es posible definir excepciones propias, las cuales no necesariamente deben
#   tener un tipo específico asociado, pero es altamente recomendado hacerlo.
# - Todas las excepciones built-in son clases derivadas de la clase base BaseException, o
#   de otras clases base derivadas de ella, mientras que todas las excepciones definidas
#   por el usuario son derivadas de la clase base Exception.




# AttributeError        Error en una referencia o asignación a un atributo.
# ImportError           Importar un módulo no encontrado.
# IndexError            Referenciar un índice fuera del rango posible en una secuencia.
# KeyError              Referenciar una clave no existente en un diccionario.
# MemoryError           Ejecución que consume toda la memoria disponible.
# NameError             Referenciar una variable no encontrada.
# TypeError             Aplicar una operación o función a un objeto de tipo incorrecto.
# ZeroDivisionError     Dividir por cero.


# try:
#     opcion = int(input('Ingrese solo números: '))
# except ValueError:  
#     print('Debe ingresar solo números') # Si detecta error, imprimer y continua
# print('Continua...')





# 1. Se debe generar una cláusula except por cada tipo de excepción para la cual se desea
#    controlar un flujo.
# 2. Una vez que se genere una excepción dentro de la cláusula try, el intérprete de Python
#    revisará, en orden de escritura, los tipos de excepciones dentro de las cláusulas except
#    que tiene asociadas.
# 3. Se ejecutará el código declarado dentro de la primera cláusula except que cumple con
#    el tipo de excepción de la excepción generada.
# 4. Si dentro de las cláusulas except declaradas no se ha incluido el tipo de la excepción
#    generada dentro de la cláusula try, entonces la excepción no será capturada,
#    provocando la interrupción del programa



consultar = True

# while consultar:
#     try:
#         edad = int(input('Ingrese su edad: '))
#         divisor = int(input('Ingrese numero para dividir edad: '))
#         print(edad / divisor)
#         consultar = False # termina si llega aquí
#     except ValueError:
#         print('>> Debe ingresar solo número!')
#     except ZeroDivisionError:
#         print('>> No puede dividir por cero!')
#     except Exception as e:
#         print(f'>> Error detectado: {e}')
#     except:
#         print('>> Error sin información')






# raise:
# Dado que el control de excepciones permite controlar el flujo de un programa, puede darse
# el caso de que el programador desee forzar que se genere una excepción en determinadas
# circunstancias.
# Esto es posible mediante la declaración raise, la cual a continuación requiere que se
# especifique el tipo de excepción a generar. Para ello, se debe indicar el tipo de la excepción
# o generar una instancia de ella.
# En caso de que se genere una instancia, se puede ingresar como argumento de su
# constructor el valor asociado de la excepción.


# consultar = True

# while consultar:
#     try:
#         edad = int(input('Ingrese edad: '))
#         if edad <= 0:
#             raise Exception('Edad debe ser un numero positivo') # Exepción creada por el usuario
#         divisor = int(input('Ingrese número para dividir su edad: '))
#         print(edad / divisor)
#         consultar = False
#     except ValueError:
#         print('Debe ingresar un número')
#     except ZeroDivisionError:
#         print('El N° por el cual desea dividir no puede ser cero')
#     except Exception as e:
#         print(f'ERROR: {e}') 
#     except: # No deja cerrar
#         print('ERROR SIN INFORMACIÓN')



# # Capturar control + c y control + d
# try:
#     edad = int(input('Ingrese edad: '))
# except Exception as e:
#     # Este bloque solo captura excepciones que son instancias de Exception o derivadas de ella
#     print("Error:", e)
# except KeyboardInterrupt:
#     # Este bloque maneja específicamente la interrupción por Control+C
#     print("Programa interrumpido por el usuario")
# except EOFError:
#     # Este bloque maneja específicamente la interrupción por Control+D
#     print("Fin de archivo (EOF) detectado")







#Crea una exepción:
# Para definir una excepción, se debe crear una clase que derive de la clase base Exception
# (o de alguna bajo su jerarquía). Como buena práctica, se sugiere crear una clase base para
# excepciones definidas, la cual luego será heredada por cada clase de excepciones propias
# que se desea generar.
# Comúnmente, las clases utilizadas para definir excepciones terminan su nombre en “Error”.





# class Error(Exception):
#     pass

# class EdadError(Error):
#     def __init__(self, mensaje, edad):
#         self.mensaje = mensaje
#         self.edad = edad

# # class EdadError(Error):
# #     pass

# consultar = True
# while consultar:
#     try:
#         edad = int(input('Ingrese edad: '))
#         if edad <= 0:
#             raise EdadError('Edad debe ser un numero positivo', edad) # Exepción creada por el usuario
#         divisor = int(input('Ingrese número para dividir su edad: '))
#         print(edad / divisor)
#         consultar = False
#     except ValueError:
#         print('Debe ingresar un número')
#     except ZeroDivisionError:
#         print('El N° por el cual desea dividir no puede ser cero')
#     except Exception as e:
#         print(f'ERROR: {e}') 
#     except KeyboardInterrupt:
#         print('Cancelado por el usuario')
#         break
#     # except: # No deja cerrar
#     #     print('ERROR SIN INFORMACIÓN')











# #Usar pass o __init__
# # La principal diferencia entre usar `pass` y definir un constructor (`__init__`) en una clase
# # de excepción personalizada en Python es la capacidad de personalizar la excepción con atributos 
# # adicionales y mensajes de error.

# # En la **Versión 1**, donde utilizas `pass`, estás creando una clase de excepción mínima que no hace
# # nada más que heredar de la clase `Exception`. No proporciona información adicional aparte del mensaje
# # de error que se pasa al momento de levantar la excepción (`raise`).

# class Error(Exception):
#     pass

# class EdadError(Error):
#     pass


# # En la **Versión 2**, defines un constructor `__init__` en tu clase de excepción personalizada. 
# # Esto te permite inicializar la excepción con atributos adicionales y almacenar más información 
# # sobre el error. Por ejemplo, en tu código, estás almacenando un mensaje y el valor de la edad que
# # causó la excepción.


# class Error(Exception):
#     pass

# class EdadError(Error):
#     def __init__(self, mensaje, edad):
#         self.mensaje = mensaje
#         self.edad = edad


# # Cuando levantas la excepción `EdadError`, puedes acceder a estos atributos en el bloque `except` para 
# # proporcionar un manejo de errores más detallado y específico. Por ejemplo:


# try:
#     # ...
#     if edad <= 0:
#         raise EdadError('Edad debe ser un numero positivo', edad)
#     # ...
# except EdadError as ee:
#     print(f'{ee.mensaje} - Edad ingresada: {ee.edad}')


# # En resumen, la **Versión 2** te permite crear excepciones más ricas y descriptivas que pueden llevar
# # consigo información adicional sobre el contexto del error, lo cual puede ser muy útil para depurar 
# # y manejar errores de manera más efectiva. La **Versión 1** es más simple y se utiliza cuando no 
# # necesitas más información que el mensaje de error estándar.






# Acciones de limpieza con finally
# Una cosa a tener en cuenta es que también es posible escribir un bloque try/finally sin cláusulas
# except. Es decir, si se añade la cláusula finally, la cláusula except pasa a ser opcional.
# Alternativamente, también es posible usar la cláusula else, la cual se ubica entre
# except y finally, y se ejecuta siempre que no ocurra ninguna excepción en el código
# definido en try o en except.

class Error(Exception):
    pass

class EdadError(Error):
    def __init__(self, mensaje, edad):
        self.mensaje = mensaje
        self.edad = edad

intentos = 0

while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        if edad < 0:
            raise EdadError("Debe ser un N° positivo.", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except EdadError as e:
        print(f"La edad '{e.edad}' no es válida. {e.mensaje}")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        intentos +=1 # Se ejecuta siempre
print(f'Los intentos fueron: {intentos}')








