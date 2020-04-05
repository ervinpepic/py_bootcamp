values = [x * 2 for x in range(10)]
for x in values:
    print(x)
# print(values)

# if we have a larger data set, we must pay atention to memory leaks,
# for that purpose we use <generator objects> that is also iterable
from sys import getsizeof
val = (x * 2 for x in range(10000000))
print("Size of generator object is: ", getsizeof(val))