numbers = [29, 34, 1, 8, 99]
numbers.sort()  # this sort lists in ascending order,
# if we want to sort in descending we must set sort(reverse=True)
# print(numbers)
# we can use sorted method to create new sorted list from our list ex:
x = sorted(numbers, reverse=True)
print(x)
print(numbers)

products = [
    ("Product_1", 8),
    ("Product_2", 20),
    ("Product_3", 13)
]

# ugly way of sorting items


def sort_products_by_price(item):
    return item[1]


products.sort(key=sort_products_by_price)
print(products)

# better way is using lambda anonymous function
# we don't need sort_product_by_price function at all

products.sort(key=lambda item: item[1])
print(products)
