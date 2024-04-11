from pizza import Pizza

print(Pizza.masas)
print(Pizza.proteinas)
print(Pizza.vegetales)

print('Está presente' if Pizza.esta_presente('salsa de tomate', ['salsa de tomate', "salsa bbq"]) == True 
    else 'No está presente')

pizza = Pizza.realizar_pedido()

print('\nIngredientes:')
print('Tipo de maza : ', pizza.masa)
print('Proteina     : ', pizza.proteina)
print('Vegetal 1    : ', pizza.vegetal_1)
print('Vegetal 2    : ', pizza.vegetal_2)
print('Tamaño       : ', pizza.tamaño)
print('Precio       : ', pizza.precio)
print('** Pizza valida **' if pizza.pizza_valida == True else '** Pizza inválida **')