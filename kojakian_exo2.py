from Exo1 import Robot

class Humain:
    def __init__(self, nom, sexe):
        self.__sexe = sexe
        self.__nom = nom
        self.__aliments = []

    def set_nom(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom
    
    def set_sexe(self, sexe):
        self.__sexe = sexe

    def get_sexe(self):
        return self.__sexe
    
    def manger(self, aliment):
        self.__aliments.append(aliment)
        print(f"L'humain mange {aliment}")

    def digerer(self):
        if len(self.__aliments) != 0:
            self.__aliments.clear()
            print("L'estomac de", self.__nom, "est vide")
        else:
            print("L'estomac de", self.__nom, "est deja vide")
        
class Cyborg(Robot, Humain):
     def __init__(self, nom, sexe):
        Robot.__init__(self, nom)
        Humain.__init__(self, nom, sexe)

    

if __name__ == "__main__":
    cyborg1 = Cyborg("Abd", "Homme")
    cyborg1.power_on()
    cyborg1.charge_battery()
    cyborg1.manger("pomme")
    cyborg1.manger("banane")
    cyborg1.manger("fraise")
    cyborg1.manger("nutella")
    cyborg1.digerer()
    cyborg1.set_speed(60)
    cyborg1.get_speed()
    cyborg1.get_status()
    cyborg1.stop()
    cyborg1.power_off()