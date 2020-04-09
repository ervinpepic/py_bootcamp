class Product:

    def __init__(self, fn_price):
        self.price = fn_price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Can't accept negative price...")
        self.__price = value


new_product = Product(-14)
print(new_product.price)

# No we use a much better solution with pythonic solution using @property decorator
