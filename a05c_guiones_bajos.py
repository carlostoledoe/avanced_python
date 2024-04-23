# El uso de guiones simples (`_`) y dobles (`__`) en Python se guía principalmente por la 
# intención de encapsulación y la necesidad de proteger el estado interno de una clase. 
# Aquí te dejo algunas recomendaciones sobre cuándo usar cada uno, según las prácticas comunes 
# en programación con Python:


# >>>> 1. Guion simple `_` (atributo protegido) <<<<
# Usa un guion simple para atributos y métodos que son destinados a ser usados solo dentro de 
# la clase y sus subclases, pero donde una fuerte restricción de acceso no es necesaria. 
# Esto sirve principalmente como una indicación para otros programadores de que ciertas partes 
# de la API son internas y no deberían ser utilizadas directamente. Por ejemplo:


#       - En bibliotecas o frameworks, donde quieres indicar a los desarrolladores que no modifiquen 
#         o accedan a ciertos atributos o métodos directamente.
#       - Cuando estás trabajando en un equipo grande y necesitas establecer claramente qué métodos o 
#         atributos no están destinados para uso externo, pero donde la subclase podría necesitar 
#         acceder a ellos.


# >>>> 2. Doble guion `__` (atributo privado) <<<<
# Utiliza doble guion para atributos y métodos que realmente quieras ocultar del exterior de la clase. 
# Python utiliza name mangling para hacer que sea mucho más difícil el acceso desde fuera de la clase, 
# aunque técnicamente aún es posible. Esto es útil cuando:

#       - Necesitas evitar que tus atributos sean sobrescritos accidentalmente, especialmente cuando hay 
#         muchas posibilidades de que el mismo nombre de atributo pueda ser usado en clases que serán 
#         extendidas por otros.
#       - Quieres reducir el riesgo de conflictos de nombres en subclases, garantizando que tus atributos 
#         privados no sean accesibles directamente por clases que heredan de la tuya.



# Ejemplos prácticos
# Imagina una clase que administra usuarios donde cierta información debe ser protegida:



# class Usuario:
#     def __init__(self, nombre, contrasena):
#         self.nombre = nombre
#         self._estado = "activo"  # Se espera que este atributo solo sea usado internamente y subclases
#         self.__contrasena = contrasena  # Esto debe ser estrictamente privado

#     def _cambiar_estado(self, estado):  # Interno, pero accesible por subclases
#         self._estado = estado

#     def __cambiar_contrasena(self, nueva_contrasena):  # Estrictamente privado
#         self.__contrasena = nueva_contrasena

#     def verificar_contrasena(self, contrasena):
#         return contrasena == self.__contrasena



# En este ejemplo, `nombre` es público y accesible sin restricciones, `_estado` y `_cambiar_estado` son 
# protegidos y deberían ser usados solo internamente o por subclases, y `__contrasena` junto 
# con `__cambiar_contrasena` son privados, protegidos contra el acceso externo y los conflictos de 
# nombres en subclases.

# Conclusión
# Elige `_` (protegido) o `__` (privado) según la necesidad de proteger tu código dentro de un proyecto.
# Recuerda que, aunque el doble guion `__` hace más difícil el acceso a atributos, no proporciona 
# seguridad completa, ya que Python no tiene verdaderos métodos o atributos privados como otros 
# lenguajes orientados a objetos. Estas convenciones son más para uso correcto según el diseño de tu 
# programa que para seguridad o privacidad real.




# # Un guión bajo
# class Ejemplo:
#     def __init__(self):
#         self._interno = 10  # Indica que es un atributo interno

# instancia = Ejemplo()
# print(instancia._interno)  # Funciona, pero no se recomienda acceder directamente






# # Doble guión bajo
# class Persona:
#     def __init__(self, nombre, rut):
#         self.__nombre = nombre
#         self.__rut = rut

# juan = Persona('Juan', 11)
# # print(juan.__rut)  # Esto generará un error AttributeError
# # print(juan._Persona__rut)  # Esto funciona debido al name mangling






