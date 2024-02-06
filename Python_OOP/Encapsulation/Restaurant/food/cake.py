from desert import Desert


class Cake(Desert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)
