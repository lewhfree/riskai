import countries
import random


class Game:
    def __init__(self, extra_territories, players: list):
        self.troop_counts = countries.troop_count
        self.ownership = countries.ownership
        self.territory_enabled = countries.enabled
        self.extra_territories = extra_territories
        self.all_extra_territories = countries.extra_territories
        self.player = players
        self.numplayers = len(self.player)
        self.over = False

    def setup(self) -> None:
        disabled_territories = [x for x in self.all_extra_territories if x not in self.extra_territories]
        for territory in disabled_territories:
            self.territory_enabled[countries.name.index(territory)] = False

        num_territories = self.territory_enabled.count(True)
        rounds = num_territories // self.numplayers
        remainder = num_territories % self.numplayers

        options = list(range(self.numplayers))
        result = []
        for i in range(self.numplayers):
            result.extend([i] * rounds)

        extra = random.sample(options, remainder)
        for i in extra:
            result.append(i)
        random.shuffle(result)

        self.ownership = result

        troops: int = (50 - 5 * self.numplayers) if self.numplayers <= 6 else (30)
        remainingtroops: list = []
        for i in range(self.numplayers):
            remainingtroops.append(troops - result[i])
        self.remaining_troops = remainingtroops

    def step(self):
        pass
