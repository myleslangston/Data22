from Animal import Animal


class Reptile(Animal):  # Inheritance - can have subclasses of a class

    def __init__(self):
        super().__init__()  # super is a keyword that relates to the Parent class (Animal)
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun at???")

    def hunt(self):
        print("Wait for it, wait for it.... POUNCE!!!")

    def use_venom(self):
        print("If I have it, I am going to use it")

    def attract_mate_through_scent(self):
        print("Time to throw on the Eau de Toilette")


jeremy_the_reptile = Reptile()
jeremy_the_reptile.breathe()  # has all the functions from the Animal class AND the Reptile class

sue_the_animal = Animal()
sue_the_animal.breathe()  # only has functions from the Animal class
