from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

class Animal:
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero) -> None:
        Animal.totalAnimales += 1
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None

    @classmethod
    def totalPorTipo(clc):
        return "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\n" + "Aves: " + str(Ave.cantidadAves()) + "\n" + "Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + "Peces: " + str(Pez.cantidadPeces()) + "\n" + "Anfibios: " +  str(Anfibio.cantidadAnfibios())

    def __str__(self) -> str:
        return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en "+ str(self.habitat) + " y mi genero es " + str(self.genero)

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def getTotalAnimales(clc):
        return clc.totalAnimales

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad
    
    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat
    
    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero
    
    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona
    


    