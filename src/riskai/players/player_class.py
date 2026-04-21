from abc import ABC, abstractmethod
from riskai.messages import Observation, Response, InvalidResponseError
from riskai.decisions import Stages


class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation: Observation, phase: Stages) -> Response:
        pass

    @abstractmethod
    def error(self, error: InvalidResponseError) -> None:
        pass
