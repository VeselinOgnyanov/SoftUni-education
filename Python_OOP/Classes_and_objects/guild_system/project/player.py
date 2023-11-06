class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        string_to_print = ""
        string_to_print += f"Name: {self.name}" + "\n"
        string_to_print += f"Guild: {self.guild}" + "\n"
        string_to_print += f"HP: {self.hp}" + "\n"
        string_to_print += f"MP: {self.mp}" + "\n"
        for key, value in self.skills.items():
            string_to_print += f"==={key} - {value}" "\n"
        return string_to_print
