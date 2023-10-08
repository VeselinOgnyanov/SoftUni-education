from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon_object in self.pokemons:
            if pokemon_name == pokemon_object.name:
                self.pokemons.remove(pokemon_object)
                return f"You have released {pokemon_name}"
            else:
                return "Pokemon is not caught"

    def trainer_data(self):
        trainer_data_string = f"Pokemon Trainer {self.name}" + "\n"
        trainer_data_string += f"Pokemon count {len(self.pokemons)}" + "\n"
        for current_pokemon in self.pokemons:
            trainer_data_string += "- " + current_pokemon.pokemon_details() + "\n"
        return trainer_data_string


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
