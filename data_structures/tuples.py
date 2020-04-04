# unlike lists, tuples cannot be changed, it's read only structure

point = (1, 2, 3)
print(point[0:1])
x, y, z = point  # we can unpack tuples
if 10 in point:
    print("OK")

# but we can't assign to tuple like this
point[1] = 3  # it would thorw an error
