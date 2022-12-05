class Personaje():
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificacion=""):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__daño = daño
        self.__bonificacion = bonificacion
    


    def __str__(self):
        return "Nombre: {} - Raza: {} - Arma: {} - Vida: {} - Daño: {} - Bonificacion: {}".format(self.__nombre, self.__raza, self.__arma, self.__vida, self.__daño, self.__bonificacion)

    def GetNombre(self):
        return self.__nombre
    def Set(self, nombre):
        self.__nombre = nombre
    
    def GetRaza(self):
        return self.__raza
    def SetRaza(self, raza):
        self.__raza = raza

    def GetArma(self):
        return self.__arma
    def SetArma(self, arma):
        self.__arma = arma
    
    def GetVida(self):
        return self.__vida
    def SetVida(self, vida):
        self.__vida = vida
    
    def GetDaño(self):
        return self.__daño
    def SetDaño(self, daño):
        self.__daño = daño
    
    def GetBonificacion(self):
        return self.__bonificacion
    def SetBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    
    def vivo(self):
        return self.__vida > 0

    def Combate(self,enemigo):
        daño = enemigo.__daño
        self.__vida = self.__vida = daño
        enemigo.__vida = enemigo.__vida - self.__daño
        print(self.__nombre, "ha realizado", self.__daño, "puntos de daño")
        if enemigo.vivo():
            print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
        else: 
            enemigo.Derrota()
    
    def Historia(self):
            pass
      
    def Victoria(self):
        return print(self.__nombre, "Ganó")
    
    def Derrota(self):
        self.__vida = 0
        return print(self.__nombre, "Ha muerto..")

    def MensajeInicial(self):
        pass