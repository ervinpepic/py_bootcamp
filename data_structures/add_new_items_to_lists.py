letters = ["a", "b", "c"]

# Adding item to lists
letters.append("D")  # apend an item to the end of the list
print(letters)
letters.insert(0, 'E')  # insert an item to list using index and item
print(letters)

# Removing item from list
letters.pop(0)  # remove item from the end of the lists
print(letters)
letters.remove("a")  # remove corresponding item from
print(letters)
del letters[0:3]  # delete a range of items
print(letters)
letters.clear()  # clear all lists
print(letters)


# Finding item in lists
letters_1 = ["a", "b", "c", "d"]

print(letters_1.count("a"))
if "a" in letters_1:
    print(letters_1.index("a"))