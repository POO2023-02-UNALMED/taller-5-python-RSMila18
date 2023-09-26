from gestion.zona import Zona
class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)
        zona.setZoo(self)

    def cantidadTotalAnimales(self):
        contador = 0
        for zona in self.zonas:
            contador += Zona.cantidadAnimales(zona)
        return contador

    def getNombre(self):
        return self.nombre

    def getUbicacion(self):
        return self.ubicacion

    def getZona(self):
        return self.zonas

    def setNombre(self, nombre):
        self.nombre = nombre

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setZona(self, zonas):
        self.zonas = zonas
