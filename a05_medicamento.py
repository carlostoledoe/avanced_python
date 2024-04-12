class Medicamento:
    iva = 0.19
    
    def __init__(self, nombre, stock = 0):
        self.nombre = nombre
        self.stock = stock
        # self.precio_bruto = 0 # Se asignan en una instancia ya creada, no al instanciar
        # self.precio_neto = 0
        # self.descto = 0
        # Atributos privado, no se pudeen modificar
        self.__precio_bruto = 0 
        self.__precio_neto = 0 
        self.__descto = 0 
    
    def asignar_precio(self, valor):
        self.__precio_bruto = valor
        if valor >= 20000:
            self.__descto = 0.2
        elif valor >= 10000:
            self.descto = 0.1
        self.__precio_neto = (self.__precio_bruto  * (1 + Medicamento.iva)) * (1 - self.__descto)
    
    @property
    def precio_bruto(self):
        return self.__precio_bruto
    @property
    def precio_neto(self):
        return self.__precio_neto
    @property
    def descto(self):
        return self.__descto
    
    @descto.setter
    def descto(self, nuevo_valor):
        self.__descto = nuevo_valor


m1 = Medicamento('Paracetamol', 5)
m2 = Medicamento('Eutirox')
m3 = Medicamento('Aspirina', 1)

m3.asignar_precio(2500)
print(m3.precio_neto)

#esto es incosistente
# m2.precio_bruto = 5000
# m2.precio_neto = 1000
