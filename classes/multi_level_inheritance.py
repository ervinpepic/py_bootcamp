class Animal:
    def eat(self):
        print("Eat...")


class Bird(Animal):
    def fly(self):
        print("Fly...")


class Chicken(Bird):
    pass

# Multi level inheritance is really bad practice
# In the example above we have bird that can fly
# chicken is also bird but can't fly...
# avoid multi level inheritance whenever you can...
# Limit inheritance to one or two classes...
