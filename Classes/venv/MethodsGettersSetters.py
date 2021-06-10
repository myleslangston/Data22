
# ENCAPSULATION - GROUPING THINGS TOGETHER


class Person:
    def __init__(self, name, age = 0):
        self.name = name
        self.__age = age

    # def display(self):
    #     print(self.name)
    #     print(self.__age)

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        self.__age = age

Ola = Person("Ola", 75)

Ola._age = 50  # it's there but hidden, can change it still - code to tell others to BACK OFF
# Ola.display()
Ola.__age = 25  # This stops anyone from changing the variable apart from the original coder. PRIVATE MODE = Dunder/Mangling

Ola.set_age(25)
Ola.get_age()
