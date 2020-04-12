# Use mulitple inheritance only when you need it.
# Mulitple inheritance as you can see bellow, allow you to
# inherit mulitple base class in sub class.

# Bello examples is bad example of using mulitple inheritance


class Employee:
    def greet(self):
        print("Hello emplyees")


class Person:
    def greet(self):
        print("Hello Person")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# Here is the good example of using mulitple inheritance


class Flyer:
    pass


class Swimmer:
    pass


class FlyFish(Flyer, Swimmer):
    pass

#These abstract class are completely independet, and each class 
# has it's own methods that describe exactly what object can do.Î