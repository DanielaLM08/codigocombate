from personaje import Personaje

class Enano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificacion="", clan=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__clan = clan

    def __str__(self):
        return super().__str__()+"Clan: {}".format(self.__clan)
        

    def GetClan(self):
        return self.__clan
    def SetClan(self, clan):
        self.__clan = clan

    
    def AumentaVida(self, vida):
        while True:
            try:
                print("¡Te ha tocado enano, puedes aumentar su vida antes de iniciar en un rango de 100 a 150!\n")
                aumenta_vida = int(input("Ingrese aumento entre 100 y 150: "))
                if aumenta_vida >=100 and aumenta_vida <=100:
                    print("Has aumentado ", aumenta_vida) 
                else:
                    break
            except ValueError:
                print("Caracter no reconocido, intenta de nuevo")
            finally:
                print("vida: ",aumenta_vida)
            return aumenta_vida + vida
    
    def Historia(self):
        return "Los humanos y elfos se han dedicado por mucho tiempo a destruir nuestras tierras y eso termina hoy."



    
