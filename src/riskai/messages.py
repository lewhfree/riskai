from dataclasses import dataclass
from enum import IntEnum


@dataclass
class Observation:
    troops: list[int]
    ownership: list[int]
    cards: list[int]
    player_id: int
    turn_number: int


@dataclass
class Response:
    current_decision: int
    response: object


# the valid responses


@dataclass
class TroopPlacement:
    territory_id: int


@dataclass
class Attack:
    do_attack: bool
    from_territory_id: int = -1
    to_territory_id: int = -1
    troops: int = -1


class TreatyLevels(IntEnum):
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    WAR = 4
    NONE = 0


@dataclass
class Treaty:
    level: TreatyLevels
    person: int = -1


@dataclass
class Cards:
    okay: bool


@dataclass
class Retreat:
    retreat: bool


@dataclass
class Fortify:
    do_reinforce: bool
    from_territory: int = -1
    to_territory: int = -1
    troops: int = -1
