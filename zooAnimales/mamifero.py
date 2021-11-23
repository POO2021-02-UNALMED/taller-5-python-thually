from zooAnimales.animal import Animal

class Mamifero (Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @classmethod
    def cantidadMamiferos(clc):
        len(clc.listado)

    @classmethod
    def crearCaballo(clc, nombre, edad, genero):
        clc.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(clc, nombre, edad, genero):
        clc.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje
    
    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

    @classmethod
    def getListado(clc):
        return clc.listado