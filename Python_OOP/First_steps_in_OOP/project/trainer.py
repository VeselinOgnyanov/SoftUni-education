from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This {pokemon} is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in 



#     • release_pokemon(pokemon_name: string)
#         ◦ Checks if you have a pokemon with that name and removes it from the collection.
# In the end, returns "You have released {pokemon_name}"
#         ◦ If there is no pokemon with that name in the collection, returns "Pokemon is not caught"
#     • trainer_data()
#         ◦ The method returns the information about the trainer and his pokemon's collection in the format:
# "Pokemon Trainer {trainer_name}
#  Pokemon count {the amount of pokemon caught}
#  - {pokemon_details1}
#  ...
#  - {pokemon_detailsN}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
