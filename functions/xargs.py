# we use *args - asterisk arguments to pass unknow number of parametars to the function
# defintion parameters. *ARGS function parameter have a TUPLE type of return value like this in example bellow:


def mulitply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


x = mulitply(2, 4, 6, 8, 12)
print(x)

# we use **kwargs when we need to use a key:value pairs, instead of returning tuple like *args,
# **kwargs return object with key:value data


def save_user(**user):
    print(user)


save_user(id=1, name="Ervin", age=26)
