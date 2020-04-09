class Product:

    def __init__(self, fn_price):
        self.set_price(fn_price)

    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        if value < 0:
            raise ValueError("Can't accept negative price...")
        self.__price = value
    
    price = property(get_price, set_price)

new_product = Product(10)
print(new_product.price)

# in the concept above, we have a lot of confusing sutff. So first
# we don't use pythonic way of solving problems. and we need to fix that
# using @property decorator and @setter decorator