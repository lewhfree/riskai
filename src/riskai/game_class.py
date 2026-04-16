import riskai.countries as countries
import random
from riskai.messages import Observation, Response


class Game:
    def __init__(self, extra_territories, players: list):
        # State
        self.troop_counts = countries.troop_count
        self.ownership = countries.ownership
        self.territory_enabled = countries.enabled

        self.extra_territories = extra_territories
        self.all_extra_territories = countries.extra_territories

        self.players = players
        self.numplayers = len(self.players)
        self.over = False
        # a list of card ids for each player
        self.cards: list[list[int]] = [[0] for _ in range(self.numplayers)]

    def start(self) -> None:
        disabled_territories = [x for x in self.all_extra_territories if x not in self.extra_territories]

        disabled_territories_index = [countries.name.index(a) for a in disabled_territories]
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

        # Maintain length constantly. Unused territories should still be in the list, just not owned.
        for index in disabled_territories_index:
            result.insert(index, -1)

        self.ownership = result

        troops: int = (50 - 5 * self.numplayers) if self.numplayers <= 6 else (30)
        remainingtroops: list = []
        for i in range(self.numplayers):
            remainingtroops.append(troops - result[i])
        self.remaining_troops = remainingtroops

        # first do the initial troop placement then go over the rest
        players_ids = list(range(self.numplayers))
        doneplacing = 0
        while not (doneplacing == self.numplayers):
            for player in players_ids:
                if self.remaining_troops[player]:
                    #
                    _ = self.players[player].decision(Observation(self.troop_counts, self.ownership, self.cards[player], 0, player, 0))
                    self.remaining_troops[player] -= 1
                    if self.remaining_troops[player] == 0:
                        doneplacing += 1

        while not self.over:
            pass
