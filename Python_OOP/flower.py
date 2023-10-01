class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
        self.current_water = 0

    def water(self, quantity):
        # self.water_requirements += quantity
        self.current_water = quantity
        if self.current_water >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
