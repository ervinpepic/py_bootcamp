numbers = [1, 2]
# print(numbers[3])  # we will ecounter an error, couse out of range of the array

# another type of exceptions can happen when user input an string
# but we expect integer. Like in the example bellow

user_input = int(input("Age? "))
# this statement will throw an error if user enter a string
# so we need to handle this type of error using try except block

try:
    user_in = int(input("Enter your age...: "))
except ValueError:
    print("Please enter age in number, not in chars or string")

# if we want more descriptive error to end users we can define this try except like this:

try:
    up = int(input("Enter your age: "))
except ValueError as ve:
    print("Please enter age in number, not in chars or string")
    print("Detail description", ve)
    print(type(ve))
else:
    print("No exception handled.")
