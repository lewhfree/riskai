import player_class


class User(player_class.PlayerTemplate):
    def __init__(self, own_id):
        self.id = own_id

    def extra_troop_placement(self, troop_map) -> str:  # takes in the map, outputs the territory key where to put another troop
        print("Here is the current troop map:\n")
        return input("Territory name you want to place a troop: ").upper()
        pass

    def retreat_in_battle(self) -> bool:  # takes in battle numbers and maybe map, returns whether to retreat
        pass

    def choice_to_icom(self) -> bool:
        pass

    def attack_phase(self) -> dict | None:
        pass

    def move_troops(self) -> dict | None:
        pass

    def icom(self) -> dict:
        pass
