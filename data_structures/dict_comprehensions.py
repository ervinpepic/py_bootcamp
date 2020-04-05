# method without using comprehensions
values = []
for x in range(5):
    values.append(x * 2)

# method with using comprehensions
values = [x * 2 for x in range(5)]

# of course we can use it with dictionaries
values = {x: x * 2 for x in range(5)}
print(values)

# and with tuples
values = (x * 2 for x in range(5))
print("Tuples values is -> ", values)  # but we get an generator object
# we will discus with generator expression in file called generator_expression.py
