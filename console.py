import game_class

numplayers = int(input("How many players? (1-8) [8]") or 8)
numplayers = numplayers if 1 <= numplayers <= 8 else exit("Entered invalid number of players (1-8): " + str(numplayers))
extra_territories_enabled: list = input("Territories you want enabled: ").upper().split()

game = game_class.Game(numplayers, extra_territories_enabled, [])

game.setup_map()
game.deploy()
print("map", game.troop_map, len(game.troop_map))

game.extra_troops()
print(game.remaining_troops)
