class Parent_1:
    pass

class Parent_2:
    pass

class Parent_3:
    pass

class Child_1(Parent_1,Parent_2):
    pass

class Child_2(Parent_2,Parent_3):
    pass

class Child_3(Child_1,Child_2,Parent_3):
    pass

print(Child_3.__mro__)

