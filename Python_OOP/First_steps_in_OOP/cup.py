class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity_to_add: int):
        if quantity_to_add <= abs(self.size - self.quantity):
            self.quantity += quantity_to_add

    def status(self):
        return abs(self.size - self.quantity)


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
