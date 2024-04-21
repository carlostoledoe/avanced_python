from te import Te

def eleccion_te():
    print('''
    Elija un tipo de té:
    
            1 --> Te negro
            2 --> Te verde
            3 --> Agua de hierbas
    ''')
    opcion = int(input('            > '))
    print('''
    Seleccione peso:
            300 --> 300 gramos
            500 --> 500 gramos
    ''')
    peso = int(input('            > '))
    return opcion, peso

def pedido_te(opcion, peso):
    tiempo, tipo, recomencacion = Te.instrucciones(opcion)
    precio = Te.get_precio(peso)
    print(f'''
    Su producto elegido es:

        Tipo de té:     {tipo}
        Formato:        {peso} gramos
        Precio:         ${precio}
        Tiempo:         {tiempo} minutos
        Recomendación:  {recomencacion}
    ''')

opcion, peso = eleccion_te()
pedido_te(opcion, peso)
