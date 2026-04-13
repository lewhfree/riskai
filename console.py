import game_class
from console_player_class import User

extra_territories_enabled: list = input("Territories you want enabled: ").upper().split()

players = []
for i in range(5):
    players.append(User(i))

game = game_class.Game(extra_territories_enabled, players)

game.setup()
print("map", game.troop_map, len(game.troop_map))
print(game.remaining_troops)
while (not game.over):
    game.step()
