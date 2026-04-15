from abc import ABC, abstractmethod

# attack/move = {
#   "from": "HAWAII",
#   "to": "JAPAN or whatever",
#   "troops": 5
# }


# icom = {
#   "playerID": 2,
#   "level": 3
# }
class PlayerTemplate(ABC):
    @abstractmethod
    def __init__(self):
        self.id: int
        pass

    def extra_troop_placement(self) -> str:  # takes in the map, outputs the territory key where to put another troop
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
