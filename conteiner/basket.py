from entity.milk import Milk
from entity.bread import Bread
from entity.orange import Orange


class Basket:
    def __init__(self, products=[]):
        if products:
            self.__products = products
        else:
            self.__products = []

    @property
    def size(self):
        return len(self.__products)

    def get_product(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__products[index]

    def add(self, product):
        if isinstance(product, (Bread, Milk, Orange)):
            self.__products.append(product)

    def __str__(self):
        msg = "List of products:"
        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__products[i])

        return msg
