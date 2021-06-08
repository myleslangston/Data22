class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."
obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())
