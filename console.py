import riskai.game_class as game_class
from riskai.players.console_player_class import User

extra_territories_enabled: list = input("Territories you want enabled: ").upper().split()

players = []
for i in range(5):
    players.append(User(i))

game = game_class.Game(extra_territories_enabled, players)

game.setup()

print("Territory owned by: ", game.ownership)
print("Territories in place: ", game.troop_counts)
print("Enabled territories: ", game.territory_enabled)

print(len(game.ownership))
print(len(game.troop_counts))
print(len(game.territory_enabled))

while not game.over:
    game.step()
