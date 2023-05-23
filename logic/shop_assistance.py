from conteiner.basket import Basket
from entity.milk import Milk
from entity.bread import Bread
from entity.orange import Orange


class ShopAssistance:
    @staticmethod
    def calcuate_total_price(basket):
        if isinstance(basket, Basket) and basket.size != 0:
            total = 0
            for i in range(basket.size):
                product = basket.get_product(i)

                if isinstance(product, Milk):
                    total += product.money

                if isinstance(product, Bread):
                    total += product.price

                if isinstance(product, Orange):
                    total += product.cost

                return total
