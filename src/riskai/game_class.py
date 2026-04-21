import riskai.countries as countries
import random
from copy import deepcopy
from riskai.messages import (
    Observation,
    Response,
    TroopPlacement,
    Attack,
)
from riskai.decisions import Stages


class Game:
    def __init__(self, extra_territories, players: list):
        # State
        self.troop_counts = deepcopy(countries.troop_count)
        self.ownership = deepcopy(countries.ownership)
        self.territory_enabled = deepcopy(countries.enabled)

        self.extra_territories = extra_territories
        self.all_extra_territories = countries.extra_territories

        self.players = players
        self.numplayers = len(self.players)
        self.over = False
        # a list of card ids for each player
        self.cards: list[list[int]] = [[] for _ in range(self.numplayers)]

        self.current_player = 0
        self.current_phase = Stages.INITIAL_PLACEMENT
        self.turn_number = 0

    def setup(self) -> None:
        disabled_territories = [
            x
            for x in self.all_extra_territories
            if x not in self.extra_territories
        ]

        disabled_territories_index = [
            countries.name.index(a) for a in disabled_territories
        ]
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
        troops: int = (
            (50 - 5 * self.numplayers) if self.numplayers <= 6 else (30)
        )
        remainingtroops: list = []
        for i in range(self.numplayers):
            remainingtroops.append(troops - self.ownership[i])
        self.remaining_troops = remainingtroops

    def step(self) -> None:
        player = self.players[self.current_player]
        phase = self.current_phase

        res = player.decision(self.get_observation(self.current_player), phase)
        self.apply_response(res, self.current_player)

        if phase == Stages.INITIAL_PLACEMENT:
            self.current_player = (self.current_player) % self.numplayers
            if all(t == 0 for t in self.remaining_troops):
                self.current_phase = Stages.TURN_START
        else:
            new_phase = (phase + 1) % (
                len(Stages) - 1
            )  # the minus one is to ignore initial placement
            if new_phase == 0:
                new_player = (self.current_player + 1) % self.numplayers
                self.current_player = new_player
            self.current_phase = new_phase

    def get_observation(self, player_id: int) -> Observation:
        return Observation(
            self.troop_counts,
            self.ownership,
            self.cards[player_id],
            player_id,
            self.turn_number,
        )

    def apply_response(self, response: Response, player_id: int) -> None:
        print(player_id, response)
        print("apply_repsonse")
        match response.current_decision:
            case Stages.TURN_START:
                print("turn start")
            case Stages.TREATY:
                print("treaty")
            case Stages.CARDS:
                print("cards")
            case Stages.REINFORCE | Stages.INITIAL_PLACEMENT:
                assert isinstance(response.response, TroopPlacement)
                territory_id: int = response.response.territory_id
                self.troop_counts[territory_id] += 1
            case Stages.ATTACK_DECLARATION:
                assert isinstance(response.response, Attack)
                print("attack")
            case Stages.RETREAT:
                print("retreat")
            case Stages.FORTIFY:
                print("fortify")
            case Stages.END_TURN:
                print("end")
            case _:
                exit("unhandled")

    def start(self) -> None:
        self.setup()
        while not self.over:
            self.step()
