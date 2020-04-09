# Class inheritance is just like in real world,
# we have parents, and children. Children inherit some genetics from parents and grandparents etc...
# In example bellow, we have Animal class
# with eat method and age atribute. This will be a parent class or base class
# bellow that class we have child or sub class Mammal which inherit eat function and
# age properties from parent class but also have own class of walking.
# the same applied for fish.

# Parent or Base class


class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("Can eat...")


# Child or sub class
class Mammal(Animal):  # this is where inheritance happen...

    def __init__(self):  # her we override constructor from animal class
        self.weight = 10
        super().__init__()  # if we don't call this supper that menas we completely override
        # constructor from animal class

    def walk(self):
        print("Walking")


# Child or sub class
class Fish(Animal):  # this is where inheritance happen...
    def swim(self):
        print("Swimming")


mammal = Mammal()
print("Age: ", mammal.age)
mammal.eat()
mammal.walk()
print(mammal.weight)

# if we want to check if this mammal variable is an instance of Mammal class(object)
# we can check that using isinstance() method
# also we have issublclass to check if we inherited class
# Also to note...All class in python is instance of OBJECT class...

print(isinstance(mammal, object))
print(issubclass(Mammal, Animal))
