"""As you can see in class_vs_instance_atributes.py file we used class attributes 
that have value across all class instances. We of course have also class methods 
and instance methods. If we want to create instance of some class with default
values always, we must define class method to save our time. In python we create class method 
with @classmehtod decorator above method definition like in example bellow """


class Point:
    # with __init__ magical class we create constructor for this class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # this is method decorator which emphasizes that bellow method will be
    # a class method.
    def zero(cls):  # by convetion we use cls as parameter name instead of self (but you can use anything)
        return cls(10, 10)  # default initial values for this class

    def draw(self):  # this is instance level method
        print(f"Point x is: {self.x}, and point y has a {self.y} pt value.")


point = Point.zero()  # this is the same as the call bellow
point.draw()
# new_point = Point(18, 21) # as this....
# new_point.draw()
