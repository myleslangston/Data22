from Snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


Ola = Python()
Aaron = Python()
Aaron.large = False  #polymorphism - can have the same class with different attributes
print(Aaron.large)
print(Ola.large)