class Zoologico:
    def __init__(self, nombre, ubicacion) -> None:
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantidadTotal = 0
        for zona in self.zonas:
            cantidadTotal += zona.cantidadAnimales()
        
        return cantidadTotal

    def getZona(self):
        return self.zonas

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion