class Car:

    def __init__(self, model, colour, mileage):
        self.model = model
        self.colour = colour
        self.mileage = mileage
        self.type = "Vehicle"
        self.noise()

    def noise(self):
        print("Vroooooom")


