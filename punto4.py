#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina1 = punto1
        self.esquina2 = punto2

    def calcular_lados(self):
        lado_x = abs(self.esquina2.x - self.esquina1.x)
        lado_y = abs(self.esquina2.y - self.esquina1.y)
        return lado_x, lado_y

    def calcular_perimetro(self):
        lado_x, lado_y = self.calcular_lados()
        return 2 * (lado_x + lado_y)

    def calcular_area(self):
        lado_x, lado_y = self.calcular_lados()
        return lado_x * lado_y

    def es_cuadrado(self):
        lado_x, lado_y = self.calcular_lados()
        return lado_x == lado_y