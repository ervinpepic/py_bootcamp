number = 100
while number > 0:
    print(number)
    number //= 2
    number /= 2
    number %= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


# infinite loop if we do not set break...
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break


def igo(num):
    return num