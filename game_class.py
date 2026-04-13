import countries
import copy
import random


class Game:
    def __init__(self, extra_territories, players: list):
        self.troop_map = copy.deepcopy(countries.territories)
        self.extra_territories = extra_territories
        self.all_extra_territories = countries.extra_territories
        self.player = players
        self.numplayers = len(self.player)
        self.over = False
        print("init")

    def setup(self):
        disabled_territories = [x for x in self.all_extra_territories if x not in self.extra_territories]
        for territory in disabled_territories:
            self.troop_map.pop(territory)

        num_territories = len(self.troop_map)
        rounds = num_territories // self.numplayers
        remainder = num_territories % self.numplayers
        options = list(range(1, self.numplayers + 1))
        result = []
        for i in options:
            result.extend([[i, 1]] * rounds)
        extra = random.sample(options, remainder)
        for i in extra:
            result.append([i, 1])
        random.shuffle(result)
        keys = list(self.troop_map.keys())
        for i in range(len(keys)):
            self.troop_map[keys[i]].extend((result[i][0], 1))

        troops: int = (50 - 5 * self.numplayers) if self.numplayers <= 6 else (30)

        remainingtroops: list = []
        for i in range(1, self.numplayers + 1):
            safe_troop_map: list[list] = self.troop_map or [[]]
            remainingtroops.append(troops - sum(1 for x in list(safe_troop_map.values()) if x[1] == i))
        self.remaining_troops = remainingtroops

    def step(self):
        pass
        # print("step")
