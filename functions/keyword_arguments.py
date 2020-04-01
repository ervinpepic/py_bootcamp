def increment(number, by):
    return number + by


result = increment(2, by=3)
print(result)


# function with default value
def increment_1(number_1, by=2):
    return number_1 * by


print(increment_1(10))
