import riskai.players.player_class as player_class
from riskai.messages import Observation, Response, TroopPlacement, InvalidResponseError, errors
from riskai.utils import inputs

class User(player_class.PlayerTemplate):
    def decision(self, observation:Observation) -> Response:
        print(observation)
        match observation.current_decision:
            case 0:
                territory_num = inputs.int_input("Where to place a troop? ")
                response = Response(0, TroopPlacement(territory_id=territory_num))
                return response
            case _:
                exit("not implemented")
        pass
    def error(self, error:InvalidResponseError) -> None:
        print("Error: ", errors[error.err_id])
