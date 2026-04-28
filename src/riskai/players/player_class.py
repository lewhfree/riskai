from abc import ABC, abstractmethod
from riskai.messages import Observation, Response, TreatyLevels
from riskai.decisions import Stages


class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation: Observation, phase: Stages) -> Response:
        pass

    @abstractmethod
    def move_troop_count(self, observation: Observation, from_t, to_t) -> int:
        pass

    @abstractmethod
    def retreat(self, observation: Observation, round: int) -> bool:
        pass

    @abstractmethod
    def accept_treaty(
        self,
        observation: Observation,
        player_id: int,
        level: TreatyLevels,
    ) -> bool:
        pass
