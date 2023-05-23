from entity.milk import Milk
from entity.bread import Bread
from entity.orange import Orange
from conteiner.basket import Basket


def main():
    basket = Basket()

    br = Bread()
    o = Orange()
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(o)
    basket.add(m)

    print(f"size = {basket.size}")
    print(basket)

    for i in range(basket.size):
        print(basket.get_product(i))


if __name__ == "__main__":
    main()


