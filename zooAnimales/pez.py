from zooAnimales.animal import Animal

class Pez (Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    @classmethod
    def cantidadPeces(clc):
        len(clc.listado)

    @classmethod
    def crearSalmon(clc, nombre, edad, genero):
        clc.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(clc, nombre, edad, genero):
        clc.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def movimiento(self):
        return "nadar"

    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas

    @classmethod
    def getListado(clc):
        return clc.listado
    