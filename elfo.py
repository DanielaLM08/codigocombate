from personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificacion="", reino=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__reino = reino

    def __str__(self):
        return super().__str__()+"Reino: {}".format(self.__reino)
        

    def GetReino(self):
        return self.__reino
    def SetReino(self, reino):
        self.__reino = reino

    def Historia():
        return "Nuestro lema siempre ha sido dejar la vida por los nuestros, llevaré la victoria a casa..."
    
    def QuitaVida(self):
        pass