from Restaurant.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams


# test_food = Food("asd", 12, 123)
# print(test_food)
