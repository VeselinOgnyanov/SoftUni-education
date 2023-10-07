class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        current_life = self.health - damage
        self.health = current_life
        if current_life <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: int):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
