class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_speed(self):
        print("The speed of "+ self.name + " is " + str(self.speed) + " km/h")     

class Car(Vehicle):
    def __init__(self, name, speed,mileage):
        super().__init__(name, speed)
        self.mileage = mileage
    
    def get_speed(self):
        print("The speed of "+ self.name + " is " + str(self.speed) + " km/h")

class Boat(Vehicle):
    def sail(self):
        print(self.name + " is sailing")

vehicle=Vehicle("Bike",45)
car=Car("Toyota",120,18)
boat=Boat("Titanic",30)
car.get_speed()


class Dog:
    def walk(self):
        print("*walking*")
    def speak(self):
        print("Woof!")

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff"
    
bobo=JackRussellTerrier()
bobo.walk()

