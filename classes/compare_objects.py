class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __gt__(self, value):
        return self.x > value.x and self.y > value.y

    def __add__(self, value):
        return Point(self.x + value.x, self.y + value.y)

    def __str__(self):
        return f"({self.x, self.y})"


new_point = Point(11, 21)
new_point_2 = Point(1, 2)
print(new_point == new_point_2)  # we've gotta false..
# so we need to fix this by implementing some magic methods
# __eq__ and __gt__ is magical methods for comparing our objects
# so after implementing these methods we can try to print

print(new_point_2 > new_point)
print(new_point_2 == new_point_2)

# if we want to add these two object we need antoher magical method
# __add__
add = new_point + new_point_2
print(add)
