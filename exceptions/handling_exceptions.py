# if we divide user input with 0 , our program will crash with
# ZeroDivisonException, we can handle it of course in more ways
# One od the ways is:
try:
    user_input = int(input("Enter your age: "))
    x = 10 / user_input
except ValueError as ve:
    print("Please enter age in number, not in chars or string")
    print("Detail description", ve)
    print(type(ve))
except ZeroDivisionError as zde:
    print("You can't divide number by 0 ", zde)
else:
    print("No exception handled.")

# but there is a better way of handling exceptions in python:
try:
    up = int(input("Enter your age: "))
    x = 10 / user_input
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("No exception handled.")

# cleaning up a little bit
# if we open a file in our program, and we need to close it
# if our program throw an exception, the file will never close
# so we use finally statement to do that

try:
    file_open = open("handling_exception.py")
    user_in = int(input("Enter your age: "))
    x = 10 / user_input
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("No exception handled.")
finally:
    file_open.close()

# cleaning a little bit more using WITH. Now, we don't need
# a finally clause as in example bellow
try:
    with open("handling_exception.py") as file:
        print("File opened...")
    user_in = int(input("Enter your age: "))
    x = 10 / user_input
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("No exception handled.")
