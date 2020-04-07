# we will define a class level attribut that will be valuable
# through all class instances like in the example bellow


class Point:
    default_color = "Black"  # this is class level variable
    # with __init__ magical class we create constructor for this class

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point x is: {self.x}, and point y has a {self.y} pt value.")

# if we change class attribute value, it will change in all instances
# of that class


Point.default_color = "Blue"

new_point = Point(18, 21)
print(new_point.default_color)  # this value is dervied from class
print(Point.default_color)
new_point.draw()

another_new_point = Point(1, 2)
print(another_new_point.default_color)  # this value is dervied from class
another_new_point.draw()
