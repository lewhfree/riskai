from abc import ABC, abstractmethod
from riskai.messages import Observation, Response

class PlayerTemplate(ABC):
    @abstractmethod
    def decision(self, observation:Observation) -> Response:
        pass
