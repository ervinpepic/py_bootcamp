
class Point:
    default_color = "Black"  # this is class level variable
    # with __init__ magical class we create constructor for this class

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point x is: {self.x}, and point y has a {self.y} pt value.")


Point.default_color = "Blue"

new_point = Point(18, 21)

# if we print this object, we will get an object address in output.
# to solve this, we need to implement object represntation __str__ magic function
# after we implement this magic method, we now can print this object to terminal output

print(new_point)
