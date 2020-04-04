# we can transform shape of lists in many ways
# One way is using iteration through list 
# and get exactly what we need like in ex bellow:
products = [
    ("Apples", 1.33),
    ("Pineapples", 8.21),
    ("Bannanas", 2.23)
]

only_prices = []

for g_p in products:
    only_prices.append([g_p[1]])

print(only_prices)

# The second way is using builtin function MAP
# One of the ways of using maps

x = map(lambda get_prices: get_prices[1], products)
for gp in x:
    print(gp)
#or we can creat a lists of prices using lists methods like this:

x_1  = list(map(lambda get_prices: get_prices[1], products))
print(x_1)