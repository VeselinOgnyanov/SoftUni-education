from food.starter import Starter


class Soup(Starter):
    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name, price, grams)


test_food = Soup("asd", 12, 123)
print(test_food)
