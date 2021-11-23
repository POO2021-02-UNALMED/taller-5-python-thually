from zooAnimales.animal import Animal

class Anfibio (Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @classmethod
    def cantidadAnfibios(clc):
        return len(clc.listado)
        
    @classmethod
    def crearRana(clc, nombre, edad, genero):
        clc.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(clc, nombre, edad, genero):
        clc.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self.colorPiel
        
    def setColorPiel(self, colorPiel):
        self.colorPiel = colorPiel
        
    def isVenenoso(self):
        return self.venenoso
    
    def setVenenoso(self, venenoso):
        self.venenoso = venenoso

    @classmethod
    def getListado(clc):
        return clc.listado
    
