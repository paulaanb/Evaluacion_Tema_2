class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    pass

def catalogar(lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__, vehiculo.__dict__)    
    pass