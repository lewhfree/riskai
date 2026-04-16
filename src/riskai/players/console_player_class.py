import riskai.players.player_class as player_class
from riskai.messages import Observation, Response, TroopPlacement, InvalidResponseError, errors
from riskai.utils import inputs


class User(player_class.PlayerTemplate):
    def decision(self, observation: Observation) -> Response:
        print(observation)
        match observation.current_decision:
            case 0:
                territory_num = inputs.int_input("Where to place a troop? ")
                response = Response(0, TroopPlacement(territory_id=territory_num))
                return response
            case 1:  # Treaty
                pass
            case 2:  # Card_turn_in
                pass
            case 3:  # reinforce
                pass
            case 4:  # attack declare
                pass
            case 5:  # in_battle_decision
                pass
            case 6:  # move_after_win
                pass
            case 7:  # fortify
                pass
            case _:
                exit("not implemented")
        return Response(-1, None)

    def error(self, error: InvalidResponseError) -> None:
        print("Error: ", errors[error.err_id], error.custom_str)
