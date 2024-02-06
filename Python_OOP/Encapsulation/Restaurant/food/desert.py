from food import Food


class Desert(Food):
    def __init__(self, name: str, price: float, grams: float, calories: float) -> None:
        super().__init__(name, price, grams)
        self.__calories = calories


    @property
    def calories(self):
        return self.__calories
