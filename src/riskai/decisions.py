from enum import IntEnum


class Stages(IntEnum):
    TURN_START = 0
    TREATY = 1
    CARDS = 2
    REINFORCE = 3
    ATTACK_DECLARATION = 4
    RETREAT = 5
    FORTIFY = 6
    END_TURN = 7
    INITIAL_PLACEMENT = 8
