class Dog:

    def __init__(self, name, colour):  # __init__ initialises the variables. Cannot be changed unless it's an argument
        self.name = name  # this is what is passed to the argument
        self.colour = colour  # this is what is passed to the argument
        self.animal_kind = "Canine"
        self.bark()

    def bark(self):
        print("woof")


Amy = Dog("Amy", "Golden")  # Instantiation = when you assign an instance to a class/ object

print(Amy.name)
print(Amy.colour)