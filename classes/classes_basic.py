# Classes are just blueprint for creating new objects,
# Class define shape, behavior and state of an object
# Objects are instances of classes.
# For example. We may have a class Dog
# Every Dog has a bark posibility, ears, eyes and so on...you've got a point...

# To create new custom class in Python programming language we use keyword class.


class PointOne:
    def draw_1(self):
        print("Draw point...")

# creating new instance or object of this class


pt = PointOne()
print(type(pt))
print(isinstance(pt, PointOne))


# to initilize this class with coordinates, we must create CONSTRUCTOR
# Constructor is a special method which is called when we create a new instance of class
# in the example bellow we create constructor in class POINT

class Point:
    # with __init__ magical class we create constructor for this class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point x is: {self.x}, and point y has a {self.y} pt value.")


new_point = Point(18, 21)
new_point.draw()
