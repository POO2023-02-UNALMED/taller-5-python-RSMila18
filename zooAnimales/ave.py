from zooAnimales.animal import Animal

class Ave(Animal):
    plural = "Aves"
    listado = []
    halcones = 0
    aguilas = 0

    def _init_(self,nombre, edad, habitat, genero, colorPlumas):
        super()._init_(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def getListado():
        return Ave.listado

    def getColorPlumas(self):
        return self.colorPlumas

    @staticmethod
    def setListado(listado):
        Ave.listado = listado

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")