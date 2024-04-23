class DimensionError(Exception):
    
    def __init__(self, message, dimension = None, max = None) -> None:
        super().__init__(message)
        self.dimension = dimension
        self.max = max
        
    def __str__(self) -> str:
        if self.dimension is None or self.max is None: 
            return super().__str__()
        elif self.dimension < 1:
            return f'La dimensión {self.dimension} de la foto no puede ser negativa'
        else:
            return f'La dimesión {self.dimension} no pude ser mayor al máximo {self.max}'

