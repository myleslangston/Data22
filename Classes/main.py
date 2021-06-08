# CLASS = UNFILLED QUESTIONNAIRE
# A way of bringing data and functionality together

class Dog:
    animal_kind = "Dolphin"  # class variable (already filled out on the questionnaire)

    def bark(self):  # function inside a class = method! self is everywhere - referring to whatever is in the class
        # without self being declared then it won't know about the assets of the class, can't reference the class
        #print(self.animal_kind)  # need self to reference the class variable
        return "woof"  # cookie cutter = template


print(Dog().animal_kind)
print(Dog.bark)  # finds where the function is saved within your device
print(Dog().bark)  # finds where the class is saved
print(Dog().bark())  # actually prints the contents

Myles = Dog()
Oscar = Dog()

print(type(Myles))
print(type(Oscar))

print(Myles.bark())
print(Oscar.bark())

Oscar.animal_kind = "Big Dog"
print(Myles.animal_kind)
print(Oscar.animal_kind)


