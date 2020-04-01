# define fucntion
# first is keyword DEFINE and then descriptive name. naming convetion is same as for variables


def greeting():
    x1 = print("hello")
    x2 = print("welcome")
    return x1, x2


greeting()


# pass parameter to function

def hello_greet(first_name, last_name):
    fn = print("Ervin")
    ln = print("Pepic")
    return fn, ln


hello_greet("Ervin", "Pepicccc")

# type of functions
# function that perform a task
# return a value


def get_greeting(name):
    return f"Hello {name}"


message = get_greeting("Ervin")

file = open("content.txt", "w")
file.write(message)
