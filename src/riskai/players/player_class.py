from abc import ABC, abstractmethod
from riskai.messages import Observation, Response
from riskai.decisions import Stages


class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation: Observation, phase: Stages) -> Response:
        pass
