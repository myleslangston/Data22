class Car:

    def __init__(self, max_speed, mileage, model, colour):
        self.max_speed = max_speed
        self.mileage = mileage  # miles per gallon
        self.model = model
        self.colour = colour
        self.fuel_tank_size = 12  # gallons of fuel
        self.fuel_level = 0
        self.speed = 0
        self.wheels = 4
        self.speed_increase = 0

    def description(self):
        print(f"This car is a {self.colour} {self.model} with a maximum speed of {self.max_speed} mph")

    def fuel_up(self):
        self.fuel_level = self.fuel_tank_size
        print("Fuel tank is now full.")

    def drive(self):
        print(f"The {self.model} is now driving")

    def refuel(self):
        print("Fuel is currently £5 a gallon.")
        new_level = int(input("How many gallons would you like to refuel? "))
        while self.fuel_tank_size - self.fuel_level <= new_level:
            print(f"Exceeded capacity, please enter an amount lower than {self.fuel_tank_size - self.fuel_level}.")
            new_level = int(input("How many gallons would you like to refuel? "))
        else:
            self.fuel_level += new_level
            print(f"This is going to cost £{5*new_level}")

    def distance_to_travel(self):  # max distance a car can travel with amount of fuel
        print(f"The maximum distance you can travel is {self.mileage * self.fuel_level}")

    def acceleration(self, speed_increase):
        self.speed_increase = 0
        if self.speed + speed_increase > self.max_speed:
            self.speed = self.max_speed
            print(self.speed)
        else:
            self.speed += speed_increase
            print(self.speed)



Ford = Car(120, 40, "Fiesta", "Red")

print(Ford.refuel())
