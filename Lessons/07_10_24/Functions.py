import randomname as rname
import random as r


class soccer_player: 
    def __init__(self, name: str, goals: int, assists: int) -> None:
        self.name = name
        self.goals = goals
        self.assists = assists
    def __str__(self) -> str:
        return f"{self.name}({self.goals},{self.assists})"

soccer_players = []

for i in range(1,20):
    soccer_players.append(soccer_player(rname.get_name(noun = ('dogs')),r.randint(1,100),r.randint(1,100)))



for player in soccer_players:
    print(player)