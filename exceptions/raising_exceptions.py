#if we test execution time of this code like this:
from timeit import timeit


code_1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be negative or 0.")
    return 10 / age

# we can avoid ValueError but it's not recomended to use in this way

try:
    calculate_xfactor(-1)
except:
    pass
"""
print("first Code ->", timeit(code_1, number=10000))

code_2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

# we can avoid ValueError but it's not recomended to use in this way


xfactor = calculate_xfactor(-1)
if xfactor is None:
    pass
"""
print("second Code ->", timeit(code_2, number=10000))
