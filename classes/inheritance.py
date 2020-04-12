# Class inheritance is just like in real world,
# we have parents, and children. Children inherit some genetics from parents and grandparents etc...
# In example bellow, we have Animal class
# with eat method and age atribute. This will be a parent class or base class
# bellow that class we have child or sub class Mammal which inherit eat function and
# age properties from parent class but also have own class of walking.
# the same applied for fish.

# Parent or Base class


from abc import ABC, abstractmethod


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


# Good Example of inheritance


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.oppened = False

    def open(self):
        if self.oppened:
            raise InvalidOperationError("Error while streaming...")
        self.oppened = True

    def close(self):
        if not self.oppened:
            raise InvalidOperationError("Stream is closed already")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading from a file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading from a network...")


class MemoryStream(Stream):
    def read(self):
        print("reading from memory stream")


mem_stream = MemoryStream()  # now it's fixed

# stream = Stream() # so..now we cant instatiate that class

# what is not good in the example above? We can instatiate the Stream base class and
# that is not what we want, we just want and need to instatiate child classes not parrent Stream class
# so we need to fix that using and abastratc class and abstract method decorator`
