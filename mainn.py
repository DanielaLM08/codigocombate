from enano import Enano
from elfo import Elfo
from humano import Humano
from random import randint



def random():
    x = 0
    while x == 0:
        var1 = randint(1,3)
        var2 = randint(1,3)
        if var1 == var2:
            print("")
        else:
            if var1 == 1:
                aliado = Enano("Minion", "Enano", "Magnum", 1000, 10, 0, "Miniminions")
                
            if var1 == 2:
                aliado = Elfo("Legolas", "Elfo", "Gunblade", 1000, 60, 0, "Elfitos")               
               
            if var1 == 3:
                aliado = Humano("Rey", "Humano", "Arpon", 1000, 60, 0, "Palacios")             
                
            if var2 == 1:
                enemigo = Enano("Minon", "Enano", "Magnum", 1000, 50, 0, "Miniminions")
                
            if var2 == 2:
                enemigo = Elfo("Elfo", "Elfo", "Gunblade", 1000, 60, 0, "Elfitos")

            if var2 == 3:
                enemigo = Humano("Rey", "Humano", "Arpon", 1000, 60, 0, "Palacios")
            
            aliado.Combate(enemigo)
            x=1

def EnterData():
    
    random()
    
EnterData()

