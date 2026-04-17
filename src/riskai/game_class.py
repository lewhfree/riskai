import riskai.countries as countries
import random
from riskai.messages import Observation, Response, InvalidResponseError


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

    def calculate_ownership(self) -> None:
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

    def initial_troop_placement(self) -> None:
        troops: int = (50 - 5 * self.numplayers) if self.numplayers <= 6 else (30)
        remainingtroops: list = []
        for i in range(self.numplayers):
            remainingtroops.append(troops - self.ownership[i])
        self.remaining_troops = remainingtroops
        players_ids = list(range(self.numplayers))
        doneplacing = 0
        while not (doneplacing == self.numplayers):
            for player in players_ids:
                # will keep trying on error, but alerts the player that you errored
                if self.remaining_troops[player]:
                    while True:
                        try:
                            response: Response = self.players[player].decision(Observation(self.troop_counts, self.ownership, self.cards[player], 0, player, 0))
                            wanted_territory_id: int = response.response.territory_id
                            if self.ownership[wanted_territory_id] == player:
                                self.troop_counts[wanted_territory_id] += 1
                            else:
                                # you don't own this
                                raise ValueError("You don't own the territory")
                            self.remaining_troops[player] -= 1
                            if self.remaining_troops[player] == 0:
                                doneplacing += 1
                            break
                        except Exception as e:
                            self.players[player].error(InvalidResponseError(0, str(e)))
                            continue

    def step(self) -> None:
        print("")

    def start(self) -> None:
        self.calculate_ownership()
        self.initial_troop_placement()
        # first do the initial troop placement then go over the rest
        while not self.over:
            self.step()
