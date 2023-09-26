from zooAnimales import Anfibio
from zooAnimales import Ave
from zooAnimales import Mamifero
from zooAnimales import Reptil
from zooAnimales import Pez

class Animal:
    totalAnimales = 0

    def _init_(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\n" + \
               "Aves: " + str(Ave.cantidadAves()) + "\n" + \
               "Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + \
               "Peces: " + str(Pez.cantidadPeces()) + "\n" + \
               "Anfibios: " + str(Anfibio.cantidadAnfibios())

    def _str_(self):
        if self.zona is None:
            return "Mi nombre es %s, tengo una edad de %d, habito en %s y mi genero es %s" % (self.nombre, self.edad, self.habitat, self.genero)
        else:
            return "Mi nombre es %s, tengo una edad de %d, habito en %s y mi genero es %s, la zona en la que me ubico es %s, en el %s" % (self.nombre, self.edad, self.habitat, self.genero, self.zona, self.zona.getZoo().getNombre())

    def getNombre(self):
        return self.nombre