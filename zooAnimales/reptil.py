from zooAnimales.animal import Animal

class Reptil (Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)

    @classmethod
    def cantidadReptiles(clc):
        return len(clc.listado)

    @classmethod
    def crearIguana(clc, nombre, edad, genero):
        clc.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(clc, nombre, edad, genero):
        clc.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def movimiento(self):
        return "reptar"

    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola

    @classmethod
    def getListado(clc):
        return clc.listado
    