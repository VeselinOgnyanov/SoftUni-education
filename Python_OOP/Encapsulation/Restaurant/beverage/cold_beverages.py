from beverage.beverage import Beverage


class ColdBeverages(Beverage):
    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price, milliliters)
