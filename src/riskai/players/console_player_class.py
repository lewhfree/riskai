import riskai.players.player_class as player_class
from riskai.messages import (
    Observation,
    Response,
    TroopPlacement,
    InvalidResponseError,
    errors,
)
from riskai.utils import inputs
from riskai.decisions import Stages


class User(player_class.PlayerTemplate):
    def decision(self, observation: Observation, phase: Stages) -> Response:
        print(observation)
        match phase:
            case Stages.TURN_START:
                print("turn start")
            case Stages.TREATY:
                print("treaty")
                pass
            case Stages.CARDS:
                print("cards")
                pass
            case Stages.REINFORCE | Stages.INITIAL_PLACEMENT:
                print("reinforce")
                territory_num = inputs.int_input("Where to place a troop? ")
                response = Response(
                    Stages.REINFORCE,
                    TroopPlacement(territory_id=territory_num),
                )
                return response
            case Stages.ATTACK_DECLARATION:
                print("declarea ttack")
                pass
            case Stages.RETREAT:
                print("retreat")
                pass
            case Stages.FORTIFY:
                print("fortify")
                pass
            case _:
                exit("not implemented")
        return Response(-1, None)

    def error(self, error: InvalidResponseError) -> None:
        print("Error: ", errors[error.err_id], error.custom_str)
