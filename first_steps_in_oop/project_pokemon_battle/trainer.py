from myprojects.python_oop.first_steps_in_oop.project_pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            result = next(filter(lambda x: x.name == pokemon_name, self.pokemons))

        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(result)
        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        pokemon_details = "\n".join(f'- {p.pokemon_details()}' for p in self.pokemons)
        return f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
{pokemon_details}"""

