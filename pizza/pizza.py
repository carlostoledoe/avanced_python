class Pizza:
    from ingredientes import proteinas, vegetales, masas
    def __init__(self, masa, proteina, vegetal_1, vegetal_2, pizza_valida, tamaño = 'Familiar', precio = 10000 ):
        self.masa = masa
        self.proteina = proteina
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.tamaño = tamaño
        self.precio = precio
        self.pizza_valida = pizza_valida
    
    @staticmethod
    def esta_presente(elemento, lista):
        return elemento in lista
    
    @staticmethod
    def realizar_pedido():
        pizza_valida = True

        masa = input('Ingresa masa (tradicional o delgada): ').lower()
        if not Pizza.esta_presente(masa, Pizza.masas): 
            print('Esa masa no existe!')
            pizza_valida = False
        
        proteina = input('Ingrese tipo de carne (pollo/vacuno/carne vegetal): ').lower()
        if not Pizza.esta_presente(proteina, Pizza.proteinas):
            print('Tipo de carne no valida!')
            pizza_valida = False
        
        vegetal_1 = input('Ingrese tipo de vegetal (aceituna, tomate, champiñon): ').lower()
        if not Pizza.esta_presente(vegetal_1, Pizza.vegetales):
            print('Tipo de vegetal no valido!')
            pizza_valida = False
        
        vegetal_2 = input('Ingrese tipo de vegetal (aceitunas, tomate, champiñon): ').lower()
        if not Pizza.esta_presente(vegetal_2, Pizza.vegetales):
            print('Tipo de vegetal no valido!')
            pizza_valida = False
        
        pizza = Pizza(masa, proteina, vegetal_1, vegetal_2, pizza_valida)
        return pizza


if __name__ == '__main__':
    pizza = Pizza.realizar_pedido()
    print(pizza.masa)
    print(pizza.proteina)
    print(pizza.vegetal_1)
    print(pizza.vegetal_2)
    print(pizza.tamaño)
    print(pizza.precio)
    print(pizza.pizza_valida)