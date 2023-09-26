from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []
    
    def _init_(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super()._init_(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
    
    def _init_(self):
        Pez.listado.append(self)
    
    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)
    
    def movimiento(self):
        return "nadar"
    
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.listado.append(salmon)
        return salmon
    
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.listado.append(bacalao)
        return bacalao
    
    def getColorEscamas(self) -> str:
        return self.colorEscamas
    
    def getCantidadAletas(self) -> int:
        return self.cantidadAletas