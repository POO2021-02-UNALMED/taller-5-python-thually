from zooAnimales.animal import Animal

class Ave (Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    @classmethod
    def cantidadAves(clc):
        return len(clc.listado)

    @classmethod
    def crearHalcon(clc, nombre, edad, genero):
        clc.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(clc, nombre, edad, genero):
        clc.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self.colorPlumas
        
    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas

    @classmethod
    def getListado(clc):
        return clc.listado
    
