import riskai.game_class as game_class
from riskai.players.console_player_class import User

extra_territories_enabled: list = (
    input("Territories you want enabled: ").upper().split()
)

players = []
for _ in range(5):
    players.append(User())

game = game_class.Game(extra_territories_enabled, players)

game.start()
