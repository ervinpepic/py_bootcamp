import random
import string

print(random.random())
print(random.randint(1, 19932))
print(random.choice([1, 2, 3]))
print(random.choices([1, 2, 3, 4, 5, 6], k=3))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

num_arrays = [1, 2, 3, 4]
random.shuffle(num_arrays)
print(num_arrays)
