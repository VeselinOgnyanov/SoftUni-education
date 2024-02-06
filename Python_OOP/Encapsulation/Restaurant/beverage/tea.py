from hot_beverages import HotBeverages


class Tea(HotBeverages):
    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price, milliliters)
