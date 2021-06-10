from Reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tounge = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tounge_to_small(self):
        print("Do I smell nice, or do I taste nice?")


Myles = Snake()
Myles.use_venom()

Oscar = Snake()
Oscar.use_tounge_to_small()


