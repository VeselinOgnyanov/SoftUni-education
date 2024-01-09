class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel = fuel
        self.horse_power = horse_power

        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: float):
        spend_fuel = self.fuel_consumption * kilometers

        if self.fuel >= spend_fuel:
            self.fuel -= spend_fuel
