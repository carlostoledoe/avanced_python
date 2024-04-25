# Distinguir la clase de una instancia
# - Recibe como primer argumento un objeto cualquiera.
# - Recibe como segundo argumento un tipo.
# - Retornará True en caso de que el objeto entregado en el primer argumento sea del tipo
#   del tipo entregado en el segundo argumento, y False en el caso contrario.


# class PelotaDeFutbol:
#     pass

# class PelotaDeTenis:
#     pass

# pdf = PelotaDeFutbol()
# pdt = PelotaDeTenis()

# if isinstance(pdf, PelotaDeTenis) == True:
#     print('Es pelota de futbo')
# else:
#     print('No es pelota de futbol')





# Al crear una instancia de una clase heredada se puede acceder a un método creado en su 
# clase padre, la instancia (self) evaluada mediante isinstance puede ser tanto de la clase padre, 
# como de cualquier clase hija que no haya sobrescrito el método donde se hace la evaluación.
# Esto permite condicionar, entre otros, valores que se pueden asignar a atributos de la instancia. 


class PelotaDeDeporte:
    def __init__(self, color: str) -> None:
        if isinstance(self, PelotaDeTenis): #Falso
            self._color = 'Amarillo'
        else:
            self._color = color
    
    @property
    def color(self) -> str:
        return self._color

class PelotaDeTenis(PelotaDeDeporte):
    pass

p = PelotaDeTenis('Rojo')

print(p.color) # Amarillo