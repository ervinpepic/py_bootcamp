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
f_p = list(filter(lambda p_i: p_i[1] >= 10, products))
print(f_p)