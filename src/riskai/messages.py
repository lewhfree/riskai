from dataclasses import dataclass


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


@dataclass
class TurnStart:
    okay: bool


@dataclass
class Treaty:
    okay: bool


@dataclass
class Cards:
    okay: bool


@dataclass
class Reinforce:
    okay: bool


@dataclass
class Retreat:
    retreat: bool


@dataclass
class EndTurn:
    okay: bool


@dataclass
class Fortify:
    okay: bool
