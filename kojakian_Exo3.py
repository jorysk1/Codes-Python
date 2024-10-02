from abc import ABCMeta, abstractmethod

class UnmannedVehicule(metaclass=ABCMeta):
    @abstractmethod
    def mission(self):
        pass

class AerialVehicule(metaclass=ABCMeta):
    @abstractmethod
    def voler(self):
        pass

class UnderseaVehicule(metaclass=ABCMeta):
    @abstractmethod
    def plonger(self):
        pass

class GroundVehicule(metaclass=ABCMeta):
    @abstractmethod
    def conduire(self):
        pass

class UAV(UnmannedVehicule, AerialVehicule):
    def mission(self):
        print("UAV: La mission en vol commence:")
    
    def voler(self):
        print("UAV: Décollage en cours...")

class UUV(UnmannedVehicule, UnderseaVehicule):
    def mission(self):
        print("UUV: La mission sous-marine commence:")
    
    def plonger(self):
        print("UUV: Plongée en cours...")

class UGV(UnmannedVehicule, GroundVehicule):
    def mission(self):
        print("UGV: La mission terrestre commence:")
    
    def conduire(self):
        print("UGV: Conduite en cours...")

def main():
    vehicules = [UAV(), UUV(), UGV()]
    for vehicule in vehicules:
        vehicule.mission()
        if isinstance(vehicule, AerialVehicule):
            vehicule.voler()
        elif isinstance(vehicule, UnderseaVehicule):
            vehicule.plonger()
        elif isinstance(vehicule, GroundVehicule):
            vehicule.conduire()

if __name__ == "__main__":
    main()
