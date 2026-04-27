import riskai.countries as countries
import random
from copy import deepcopy
import riskai.messages as m
# from riskai.messages import *
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
        self.deadplayers = []

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
            remainingtroops.append(troops - self.ownership.count(i))
        self.remaining_troops = remainingtroops

    def owns_continent(self, player_id, continent_id) -> bool:
        numcountries = countries.continent.count(continent_id)
        count = 0
        assert numcountries != 0
        for i, ownership in enumerate(self.ownership):
            if (ownership == player_id) and (
                countries.continent[i] == continent_id
            ):
                count += 1
        return numcountries == count

    def owns_any_continents(self, player_id) -> list[int]:
        # TODO: REALLY REALLY INEFFICIENT, FIX ASAP
        # this loops over continent #continents times. This can be simplified into a single run.
        # nested loop bad.
        owns = []
        for continent in range(countries.continent_count):
            if self.owns_continent(player_id, continent):
                owns.append(continent)
        return owns

    def step(self) -> None:
        if self.current_player in self.deadplayers:
            self.current_player = (self.current_player + 1) % self.numplayers
            self.current_phase = Stages.TURN_START
            return
        match self.current_phase:
            # ====================================================================
            # ====================================================================
            case Stages.INITIAL_PLACEMENT:
                while self.remaining_troops[self.current_player] == 0:
                    self.current_player = (
                        self.current_player + 1
                    ) % self.numplayers
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.TroopPlacement)
                territory_id: m.Response = res.response.territory_id

                self.troop_counts[territory_id] += 1
                self.remaining_troops[self.current_player] -= 1
                self.current_player = (
                    self.current_player + 1
                ) % self.numplayers
                if sum(self.remaining_troops) == 0:
                    self.current_phase = Stages.TURN_START
                    self.current_player = 0
            # ====================================================================
            # ====================================================================
            case Stages.TURN_START:
                # don't have to do anything. Just for game engine i think
                # calculate the troop numbers here
                self.current_phase = Stages.TREATY
                remaining_troops = max(
                    3, self.ownership.count(self.current_player) // 3
                )
                # this is += because there may be troops leftover from like cards
                self.remaining_troops[self.current_player] += remaining_troops
                # continent bonuses
                for owned in self.owns_any_continents(self.current_player):
                    self.remaining_troops[self.current_player] += (
                        countries.continent_bonuses[owned]
                    )
            # ====================================================================
            # ====================================================================
            case Stages.TREATY:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Treaty)
            # ====================================================================
            # ====================================================================
            case Stages.CARDS:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Cards)
            # ====================================================================
            # ====================================================================
            case Stages.REINFORCE:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Reinforce)
            # ====================================================================
            # ====================================================================
            case Stages.ATTACK_DECLARATION:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Attack)
            # ====================================================================
            # ====================================================================
            case Stages.RETREAT:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Retreat)
            # ====================================================================
            # ====================================================================
            case Stages.FORTIFY:
                current_player = self.players[self.current_player]
                res = current_player.decision(
                    self.get_observation(self.current_player),
                    self.current_phase,
                )
                assert isinstance(res.response, m.Fortify)
            # ====================================================================
            # ====================================================================
            case Stages.END_TURN:
                self.current_phase = Stages.TURN_START
                self.current_player = (
                    self.current_player + 1
                ) % self.numplayers
            # ====================================================================
            # ====================================================================
            case _:
                exit("unmatched phase")

    def get_observation(self, player_id: int) -> m.Observation:
        return m.Observation(
            self.troop_counts,
            self.ownership,
            self.cards[player_id],
            player_id,
            self.turn_number,
        )

    def start(self) -> None:
        self.setup()
        while not self.over:
            self.step()
