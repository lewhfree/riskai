from abc import ABC, abstractmethod
from riskai.messages import Observation, Response, InvalidResponseError


class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation: Observation) -> Response:
        pass

    @abstractmethod
    def error(self, error: InvalidResponseError) -> None:
        pass
