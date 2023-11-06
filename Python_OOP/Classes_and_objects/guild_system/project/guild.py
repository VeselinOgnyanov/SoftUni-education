from player import Player


class Guild:
    def __init__(self, name) -> None:
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        else:
            self.players.remove(player_name)
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        string_to_print = f"Guild: {self.name}" + "\n"
        for current_player in self.players:
            string_to_print += current_player.player_info()
        return string_to_print


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
