# Set is similar to lists and arrays in python, but with no duplicate elements
# like in example bellow:

set_of_numbers = [1, 1, 2, 3, 4, 5, 6, 4, 4, 4, 4, 4, 4]
x = set(set_of_numbers)
print(x)

# of course we can add and remove items from sets
# using add and remove set methods

x.add(10)
print(x)
x.remove(5)
print(x)
print(len(x))

# Where sets shine is in mathematical operation with sets like in ex bellow:

first_set = {1, 2, 3, 4, 5, 6, 5, 5, 6, 1, 7, 9}
second_set = {1, 3, 4, 5, 1, 2, 6, 622, 3, 3, 8}

print("Unique elements that is both in first and second set - ",
      first_set | second_set)
print("All elements that is included both in first and second set",
      first_set & second_set)
print("Elements of first but not of second set",
      first_set - second_set)
print("Elements thats either in first or second set",
      first_set ^ second_set)
