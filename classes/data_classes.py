# If we need class that don't have a methods, just data...better for us is to use
# named tupples...which is easier for memory and easier for comparison

# so ..first we need to import that
from collections import namedtuple

Point  = namedtuple("Point", ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)