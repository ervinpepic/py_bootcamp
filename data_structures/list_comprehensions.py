products = [
    ("Product_1", 8),
    ("Product_2", 2),
    ("Product_3", 13),
    ("Product_3", 16),
    ("Product_3", 1),
    ("Product_3", 98),
    ("Product_3", 54),
    ("Product_3", 3)
]
# this is the standard way of filtering and maping over lists
prices = list(map(lambda get_items: get_items[1], products))
filtered_products = list(
    filter(lambda get_items: get_items[1] >= 10, products))
print(prices, filtered_products)

# the most convinient way is using lists comprehnsions

prices_1 = [get_items_prices[1]
            for get_items_prices in products]  # instead of using map method
print("Instead of using map >>", prices_1)

filtered_products_1 = [get_filtered_products for get_filtered_products in products
                       if get_filtered_products[1] >= 10]  # Instead of using filter()
print("Instead of using filter() >>", filtered_products_1)
