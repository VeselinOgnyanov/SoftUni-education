class Customer:
    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self) -> str:
        dvd_names = [d.name for d in self.rented_dvds]
        str_to_print = f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
        str_to_print += f"rented DVD's ({', '.join(dvd_names)})"
        return str_to_print
