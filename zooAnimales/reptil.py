from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    listado = []
    
    def init(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().init(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)
    
    def movimiento(self):
        return "reptar"
    
    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)
    
    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.listado.append(iguana)
        return iguana
    
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.listado.append(serpiente)
        return serpiente
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola