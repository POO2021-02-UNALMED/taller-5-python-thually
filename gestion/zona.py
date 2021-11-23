from zooAnimales import animal


class Zona:
    def __init__(self, nombre, zoo = None) -> None:
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, ani):
        self.animales.append(ani)
        ani.setZona(self)

    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo