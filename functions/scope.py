# scope of variables outside and inside function are not connected
# except when you use GLOBAL keyword and then redefine it inside function body

message = "Ervin"  # global variable


def hello(name):
    global message
    message = "b"


hello("Pepic")
print(message)
