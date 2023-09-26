from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    listado = []
    
    def _init_(self, nombre, edad, habitat, genero, pelaje, patas):
        super()._init_(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
    
    def _init_(self):
        Mamifero.listado.append(self)
    
    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)
    
    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.listado.append(caballo)
        return caballo
    
    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.listado.append(leon)
        return leon
    
    def isPelaje(self):
        return self.pelaje
    
    def getPatas(self):
        return self.patas