class Mascota:
    def __init__(self, especie, precio, cantidad):
        self.especie = especie
        self.precio = precio
        self.cantidad = cantidad

    def get_monto_total(self): 
        return self.precio * self.cantidad  #tengo que acceder a la entidad

    def __str__(self) -> str:
        return f'{self.especie.upper()}: // Precio: ${self.precio} // Cantidad: {self.cantidad}'
    
    def __iadd__(self, otro_valor: int):
    # Sobrescritura de método += 
        print(self)
        self.cantidad += otro_valor
        return self


class Tienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.inventario = [] # Inicializamos con una lista vacía

    # def add_mascota(self, especie, precio, cantidad):
    #     nueva_mascota = Mascota(especie, precio, cantidad)
    #     self.inventario.append(nueva_mascota)

    def add_mascota(self, *mascota):
        # self.inventario.append(mascota) #agrega solo 1
        self.inventario.extend(mascota) #agrega varios
        

    def vender(self, nombre_especie):
        for mascota in self.inventario:
            if mascota.especie == nombre_especie:
                # Si la encuentro
                if mascota.cantidad > 0:
                    mascota.cantidad -= 1
                    print(f'{mascota.especie} ha sido vendida')
                else:
                    print(f'No nos quedan {nombre_especie}')
                return
        print(f'No vendemos {nombre_especie}')

    def get_activos_mascotas(self):
        # todo el dinero que tengo en mascotas
        total = 0
        for mascota in self.inventario:
            total += mascota.get_monto_total()
        return total

    def mostrar_inventario(self):
        for mascota in self.inventario:
            print(mascota)



if __name__ == '__main__':
    tienda1 = Tienda('Pikachu Store')

    alpaca = Mascota('Alpaca', 100000, 2)
    tortuga = Mascota('Tortuga Marina', 10000, 10)
    loro = Mascota('Loro', 2000, 5)
    perro = Mascota('Perro', 1000, 5)

    alpaca += 1 # A qué sumo? Puedo modificar el operador +=

    # Agrego las mascotas todas juntas
    tienda1.add_mascota(alpaca, tortuga, loro, perro)
    print(alpaca)

    # # Se agregan una a una
    # tienda1.add_mascota('Tortuga Marina', 10000, 10)
    # tienda1.add_mascota('Loro', 2000, 5)
    # tienda1.add_mascota('Perro', 1000, 5)

    tienda1.vender('Loro')
    tienda1.vender('Avestruz')

    print(tienda1.get_activos_mascotas())
    tienda1.mostrar_inventario()