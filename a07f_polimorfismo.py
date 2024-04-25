# Polimorfismo
# El polimorfismo se refiere a la capacidad de “tener varias formas”

# En programación orientada a objetos, el polimorfismo se refiere a este mismo concepto,
# considerando que la “forma” corresponde al comportamiento de un objeto, es decir, el
# polimorfismo se refiere a que el comportamiento del objeto cambia, según la clase de
# origen del objeto desde el cual se está llevando a cabo. 

# Supongamos un caso de herencia simple entre una clase padre y una clase hija, donde
# ambas han definido un mismo método. Al crearse una instancia de la clase hija, y realizar
# en ella un llamado al método definido en ambas clases, el método que se ejecutará será el
# definido en la clase hija.

#  El polimorfismo es un principio de la programación orientada a objetos que permite que objetos 
#  de diferentes clases sean tratados como objetos de una clase común

class Animal:
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

def escuchar_animal(animal):
    print(animal.hablar())

# Instancias de las clases
perro = Perro()
gato = Gato()

# Polimorfismo en acción
escuchar_animal(perro)  # Salida: Guau!
escuchar_animal(gato)   # Salida: Miau!


# En este código, Animal es la clase base y Perro y Gato son clases derivadas 
# que sobrescriben el método hablar. La función escuchar_animal puede recibir 
# cualquier objeto que sea un Animal y llamar al método hablar, sin importar de 
# qué tipo de Animal se trate. 
# Esto es polimorfismo: la capacidad de utilizar objetos de diferentes clases 
# a través de una interfaz común.