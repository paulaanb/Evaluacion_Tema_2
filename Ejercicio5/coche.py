class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    
