class Te:
    duracion = 365

    @staticmethod
    def instrucciones(tipo_te: int):
        '''
        tipo_te = 1 --> Te negro
        tipo_te = 2 --> Te verde
        tipo_te = 3 --> Agua de hierbas
        '''
        if tipo_te == 1:
            return 3, 'Té negro', 'Se recomienda tomar en la mañana'
        elif tipo_te == 2:
            return 5, 'Té verde', 'Se recomienda tomar al almuerzo'
        else:
            return 6, 'Agua de hiervas', 'Se recomienda tomar al atadecer'
    
    @staticmethod
    def get_precio(peso):
        if peso == 300:
            return 3000
        else: #peso == 500
            return 5000
