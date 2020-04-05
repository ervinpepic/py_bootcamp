# Dictionaries is the key: value pairs data structure that
# every key has a one or more values
points = {"x": 1, "y": 2}
# or we can use function dict()
points_1 = dict(y=1, x=2)
points_1["x"] = 50
points_1["y"] = 10
print(points_1)
points_1["z"] = 12
print(points_1)
# print(points_1["a"])  # if we don't have a key that we looking for
# we will get an error, to avoid this error we must use if or get()
if "a" in points_1:
    print(points_1["a"])
# or with get()
print(points_1.get("a"), "No key found")

# if we want to delete some key from our dictionaries we have to use del() method

del points_1["z"]
print("After deletion", points_1)

# iterate over dictionaries
# one way
for key in points_1:
    print("First way of iteration over dict -> ", key, points_1[key])

# second way
for key, value in points_1.items():
    print("Second way of iteration over dict -> ", key, value)
