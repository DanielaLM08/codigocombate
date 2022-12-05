from personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=150, daño="", bonificacion="", familia=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__familia = familia

    def __str__(self):
        return super().__str__()+"Familia: {}".format(self.__familia)
        

    def GetFamilia(self):
        return self.__familia
    def SetFamilia(self, familia):
        self.__familia = familia
     
    def Historia(self):
        return "El ADN de mis ancestros esta en mi sangre... Ellos siempre han derrotado cualquier cosa que se les cruce en su camino."

    def SuperBono(self):
        pass