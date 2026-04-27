from abc import ABC, abstractmethod
from riskai.messages import Observation, Response, TreatyLevels
from riskai.decisions import Stages


class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation: Observation, phase: Stages) -> Response:
        pass

    @abstractmethod
    def accept_treaty(
        self,
        observation: Observation,
        from_player_id: int,
        level: TreatyLevels,
    ) -> bool:
        pass
