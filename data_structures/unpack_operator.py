values = list(range(10))
values = [*range(20), *"Ervin"]
print(values)

# Also we can unpack and combine dictionaries using **kwargs as in example bellow

first_dict = {"x": 10}
second_dict = {"y": 11}
combined = {**first_dict, ** second_dict, "z": 12}
print(combined)