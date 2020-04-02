# we have a vast variety way to create a list:

letters = ["a", "b", "c"]  # Using characters
matrix = [[1, 2], [3, 4], [5, 6]]
""" matrix is two dimensional array, we have multiple lists 
    inside one major list, we have a rows and colums 
    just like in table"""
zeros = [0] * 5  # when we want to create more then one elements, we can multipy lists items
combined = zeros + letters  # we can concatinate them in one list
numbers = list(range(40))  # create a new list from zero to 39
chars = list("Hello there")

print(
    letters,
    matrix,
    zeros,
    combined,
    numbers,
    chars,
    len(chars)
)

# Access items in lists

letters_1 = ["a", "b", "c"]
letters_1[0] = "A"
print(letters_1)
print(letters_1[::2])

numbers_1 = list(range(20))
print(numbers_1[::2])  # or ::-1 in reverse order


# unpacking lists
numbers_2 = [1, 2, 3]

# we can unpack each elemnt and assign them to the variable like this examples bellow

first, second, third = numbers_2

# or on unrecommended way

# first = [0]
# second = [1]
# third = [2]
# if we have more komplex list but we need just a few values from that lists 
# we can use *args syntax to solve that like this in example bellow:

numbers_3 = [1, 2, 4, 5, 8, 12 ,15, 17]
fv, sc, *rest = numbers_3

print(fv, rest)

# using loops on lists

array_of_elements = ["Some words to print"]
for items, arr in enumerate(array_of_elements):
    print(items, arr)