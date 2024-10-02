import time
print(time.time())

class Robot():
    def __init__(self, name):
        self.__name = name
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0
        self.__states = ['eteint', 'allume']

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def power_on(self):
        if not self.__power:
            self.__power = True
            print(f"{self.__name} est allume")
        else:
            print(f"{self.__name} est deja allume")


    def power_off(self):
        if self.__power:
            self.__power = False
            print(f"{self.__name} est eteint")
        else:
            print(f"{self.__name} est deja eteint")

    def charge_battery(self):
        if self.__battery_level >= 100:
            print(" La batterie est deja chargee")
        else:
            print("Chargement...")
            while self.__battery_level < 100:
                time.sleep(1)
                self.__battery_level += 10
                print(f"Niveau de batterie: {self.__battery_level}%")
            print("La batterie est totalement chargee")

        
    def set_speed(self, speed):
        if self.__power:
            if speed >= 0:
                self.__current_speed = speed
                print(f"La vitesse est de {self.__current_speed} km/h.")
            else:
                print(f"{self.__name} est eteint.")

    def get_speed(self):
        return self.__current_speed
    
    def stop(self):
        if self.__current_speed > 0:
            self.__current_speed = 0
            print(f"{self.__name} est arrete")
        else:
            print(f"{self.__name} est en fonctionnement")

    def get_status(self):
        if (self.__power == True):
            state = self.__states[1]
        else:
            state = self.__states[0]
        print(f"{self.__name}", "est", state,"charge a", self.__battery_level,"%","et roule a une vitesse de", self.__current_speed, "km/h")
            

if __name__ == "__main__":
    robot = Robot("Abd")
    robot.power_on()
    robot.charge_battery()
    robot.set_speed(10)
    robot.get_status()
    robot.power_off()




    

