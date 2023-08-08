#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self):
        return f"Vehículo - Velocidad Máxima: {self.velocidad_maxima} km/h, Kilometraje: {self.kilometraje} km"
